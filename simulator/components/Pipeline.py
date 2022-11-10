import simulator.components as comp

def fetch(reg_file: comp.RegisterFile, i_mem: comp.InstructionMemory, no_of_instructions: int, instruction: int) -> bool:
    '''
    Requests the instruction memory for the instruction to which the program counter points.\n 
    Returns True once instruction is fetched and stored in the FD_intermediate.\n
    Returns False if program counter points to an instruction beyond those in the program, 
    if FD_intermediate is already filled or if instruction memory is processing the request.\n
    '''
    pc = reg_file.program_counter.getValue()
    
    if (pc / 4) >= no_of_instructions:
        return False

    response = i_mem.readData(pc)
    
    if not response:
        # print("f")
        return False
    
    if comp.FD_intermediate:
        # print("f")
        return False
    
    comp.FD_intermediate = response

    if comp.FD_intermediate[-7:] == "1100011":
        comp.BEQ_instructions.append(pc)
        comp.BEQ_instructions.append(instruction)

    # print("f")
    
    return True


def decode(reg_file: comp.RegisterFile) -> bool:
    '''
    Decodes the fetched instruction stored in FD_intermediate.\n
    Returns True after storing decoded parts in DX_intermediates for use by the execute stage.\n
    Returns False in case of data dependencies
    Returns False if DX_intermediate is already filled or if FD_intermediate is empty (there is no instruction to decode).\n
    '''
    if comp.DX_intermediate:
        # print("d")
        return False
    
    if not comp.FD_intermediate:
        return False
    
    # for STORENOC
    if comp.FD_intermediate == "00000000000000000111000001010101":
        comp.DX_intermediate['STORENOC'] = True
        # print("d")
        return True

    # immediate bits for ADDI or offset bits for LW, converted to an unsigned integer which will later be sign-extended
    imm = int(comp.FD_intermediate[-32:-20], 2)

    # offset bits for SW, converted to an unsigned integer which will later be sign-extended
    sw_offset   = int(comp.FD_intermediate[-32:-25] + comp.FD_intermediate[-12:-7], 2)

    # offset bits for BEQ, converted to an unsigned integer which will later be sign-extended
    beq_offset  = int(comp.FD_intermediate[-32] + comp.FD_intermediate[-8] + comp.FD_intermediate[-31:-25] + comp.FD_intermediate[-12:-8], 2)
    
    # fields for identifying the operation
    funct7 = comp.FD_intermediate[-32:-25]
    funct3 = comp.FD_intermediate[-15:-12]
    opcode = comp.FD_intermediate[-7:]
    
    # source and destination register numbers (index values for the list of register file's general purpose registers)
    rs2 = int(comp.FD_intermediate[-25:-20], 2)
    rs1 = int(comp.FD_intermediate[-20:-15], 2)
    rd  = int(comp.FD_intermediate[-12:-7], 2)

    # only the fields relevant to the instruction being decoded are used to fill DX_intermediate
    
    # for operations 'ADD', 'SUB', 'AND', 'OR', 'SLL', 'SRA'
    if (opcode == "0110011"):
        if not reg_file.gen_registers[rs1].available:
            # print("d")
            return False
        if not reg_file.gen_registers[rs2].available:
            # print("d")
            return False

        comp.DX_intermediate['type']        = 'R'
        comp.DX_intermediate['rs1_data']    = reg_file.gen_registers[rs1].getValue()
        comp.DX_intermediate['rs2_data']    = reg_file.gen_registers[rs2].getValue()
        comp.DX_intermediate['funct']       = funct7 + funct3
        reg_file.gen_registers[rd].toggleAvailability()
        comp.DX_intermediate['rd']          = rd
        # print("d")
        return True

    # for operation 'BEQ'
    if (opcode == "1100011"):
        if not reg_file.gen_registers[rs1].available:
            # print("d")
            return False
        if not reg_file.gen_registers[rs2].available:
            # print("d")
            return False

        comp.DX_intermediate['type']        = 'U'
        comp.DX_intermediate['rs1_data']    = reg_file.gen_registers[rs1].getValue()
        comp.DX_intermediate['rs2_data']    = reg_file.gen_registers[rs2].getValue()
        comp.DX_intermediate['beq_offset']  = beq_offset
        comp.DX_intermediate['operation']   = opcode
        # print("d")
        return True

    # for operation 'SW'
    if (funct3 + opcode) == '0100100011':
        if not reg_file.gen_registers[rs1].available:
            # print("d")
            return False
        if not reg_file.gen_registers[rs2].available:
            # print("d")
            return False
    
        comp.DX_intermediate['type']        = 'I'
        comp.DX_intermediate['rs1_data']    = reg_file.gen_registers[rs1].getValue()
        comp.DX_intermediate['rs2_data']    = reg_file.gen_registers[rs2].getValue()
        comp.DX_intermediate['imm']         = sw_offset
        comp.DX_intermediate['operation']   = funct3 + opcode
        # print("d")
        return True
    
    # for LOADNOC
    if (funct3 + opcode) == '1010101010':
        if not reg_file.gen_registers[rs1].available:
            # print("d")
            return False
        if not reg_file.gen_registers[rs2].available:
            # print("d")
            return False
    
        comp.DX_intermediate['type']        = 'I'
        comp.DX_intermediate['rs1_data']    = reg_file.gen_registers[rs1].getValue()
        comp.DX_intermediate['rs2_data']    = reg_file.gen_registers[rs2].getValue()
        comp.DX_intermediate['imm']         = sw_offset
        comp.DX_intermediate['operation']   = funct3 + opcode
        # print("d")
        return True
    
    # for operations 'ADDI', 'LW'
    else:
        if not reg_file.gen_registers[rs1].available:
            # print("d")
            return False
    
        comp.DX_intermediate['type']        = 'I'
        comp.DX_intermediate['rs1_data']    = reg_file.gen_registers[rs1].getValue()
        reg_file.gen_registers[rd].toggleAvailability()
        comp.DX_intermediate['rd']          = rd
        comp.DX_intermediate['imm']         = imm
        comp.DX_intermediate['operation']   = funct3 + opcode
        # print("d")
        return True


def execute():
    '''
    Computes the arithmetic/logical parts of the operation specified by DX_intermediate.\n
    Invokes functions defined in the ALU module to compute the final result of operations 'ADD', 'SUB', 'AND', 'OR', 'SLL', 'SRA', 'ADDI'
    and to compute the memory address accessed by 'LW' and 'SW'.\n
    Evaluates the equality condition in case of 'BEQ' and returns increment for program counter if the equality condition is satisfied.\n
    Returns False if XM_intermediate is already filled or if DX_intermediate is empty (there is no decoded instruction to execute).
    '''
    if comp.XM_intermediate:
        # print("x")
        return False
    
    if not comp.DX_intermediate:
        return False
    
    if 'STORENOC' in comp.DX_intermediate:
        comp.XM_intermediate['STORENOC'] = True
        # print("x")
        return True

    # for operations 'ADD', 'SUB', 'AND', 'OR', 'SLL', 'SRA'
    if (comp.DX_intermediate['type'] == 'R'):
        comp.XM_intermediate['type']        = comp.DX_intermediate['type']
        comp.XM_intermediate['res']         = comp.getResult(comp.DX_intermediate['rs1_data'],
                                                             comp.DX_intermediate['rs2_data'],
                                                             comp.DX_intermediate['funct'],
                                                             'R')
        comp.XM_intermediate['rd']          = comp.DX_intermediate['rd']
        # print("x")
        return True

    # for operations 'SW', 'LOADNOC'
    if (comp.DX_intermediate['operation'] == "0100100011") or (comp.DX_intermediate['operation'] == "1010101010"):
        comp.XM_intermediate['type']        = comp.DX_intermediate['type']
        comp.XM_intermediate['res']         = comp.getResult(comp.DX_intermediate['rs1_data'],
                                                             comp.DX_intermediate['imm'],
                                                             None,
                                                             'I')
        comp.XM_intermediate['rs2_data']    = comp.DX_intermediate['rs2_data']
        comp.XM_intermediate['operation']   = comp.DX_intermediate['operation']
        # print("x")
        return True

    # for operations 'ADDI', 'LW'
    if (comp.DX_intermediate['type'] == 'I'):
        comp.XM_intermediate['type']        = comp.DX_intermediate['type']
        comp.XM_intermediate['res']         = comp.getResult(comp.DX_intermediate['rs1_data'],
                                                             comp.DX_intermediate['imm'],
                                                             None,
                                                             'I')
        comp.XM_intermediate['rd']          = comp.DX_intermediate['rd']
        comp.XM_intermediate['operation']   = comp.DX_intermediate['operation']
        # print("x")
        return True

    # for operation BEQ
    if (comp.DX_intermediate['operation'] == "1100011"):
        if (comp.DX_intermediate['rs1_data'] == comp.DX_intermediate['rs2_data']):
            comp.XM_intermediate['type'] = comp.DX_intermediate['type']
            # print("x")
            return comp.getResult(0, comp.DX_intermediate['beq_offset'], None, 'U')
        # print("x")
        return True


def memory(d_mem: comp.DataMemory):
    '''
    Handles memory accesses for operations 'LW', 'SW', 'LOADNOC' and 'SENDNOC'.\n
    Transfers XM_intermediate as is to MW_intermediate for operations 'ADD', 'SUB', 'AND', 'OR', 'SLL', 'SRA', 'ADDI', 'BEQ'.
    '''

    if comp.MW_intermediate:
        # print("m")
        return False
    
    if not comp.XM_intermediate:
        return False
    
    # for 'STORENOC'
    if 'STORENOC' in comp.XM_intermediate:
        write_complete = d_mem.writeData(16400, 1)
        
        if not write_complete:
            # print("m")
            return False
        
        comp.MW_intermediate['STORENOC']       = True
        # print("m")
        return True

    # for operation 'BEQ'
    if comp.XM_intermediate['type'] == 'U':
        comp.MW_intermediate['type'] = comp.XM_intermediate['type']
        # print("m")
        return True

    # for operations 'ADD', 'SUB', 'AND', 'OR', 'SLL', 'SRA', 'ADDI' 
    if ('operation' not in comp.XM_intermediate) or (comp.XM_intermediate['operation'] == "0000010011"):
        comp.MW_intermediate['rd']          = comp.XM_intermediate['rd']
        comp.MW_intermediate['res']         = comp.XM_intermediate['res']
        # print("m")
        return True
    
    # for operation 'LW'
    if comp.XM_intermediate['operation'] == "0100000011":
        loaded_data = d_mem.readData(comp.XM_intermediate['res'])

        if not loaded_data:
            # print("m")
            return False
         
        loaded_data = int(loaded_data, 2)
        if loaded_data >= 2 ** 31:
            loaded_data -= 2 ** 32

        comp.MW_intermediate['res']         = loaded_data
        comp.MW_intermediate['rd']          = comp.XM_intermediate['rd']
        # print("m")
        return True
    
    # for operation 'SW', 'LOADNOC'
    if (comp.XM_intermediate['operation'] == "0100100011") or (comp.XM_intermediate['operation'] == "1010101010"):
        write_complete = d_mem.writeData(comp.XM_intermediate['res'], comp.XM_intermediate['rs2_data'])
        
        if not write_complete:
            # print("m")
            return False
        
        comp.MW_intermediate['operation']       = comp.XM_intermediate['operation']
        # print("m")
        return True


def writeback(reg_file: comp.RegisterFile):
    if not comp.MW_intermediate:
        return False

    if 'rd' in comp.MW_intermediate:
        # print("w")
        reg_file.gen_registers[comp.MW_intermediate['rd']].setValue(comp.MW_intermediate['res'])
        reg_file.gen_registers[comp.MW_intermediate['rd']].toggleAvailability()
        return True
    
    # print("w")
    return True