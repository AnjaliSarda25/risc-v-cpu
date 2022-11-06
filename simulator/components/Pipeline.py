from simulator.components.Register import Register

# Store fetched instruction
FD_intermediate = Register()

# Store decoded parts of fetched instruction in respective fields
DX_intermediates = {
    'opcode':Register(8), 
    'rs1':Register(5), 
    'rs2':Register(5), 
    'func3':Register(3),
    'func7':Register(7),
    'imm':Register(), 
    'rd':Register(5),
    'mem_addr':Register()
    }

XM_intermediates = {
    'mem_addr':Register(),
    'rd':Register()
    }

# Store address of register here
MW_intermediate = Register()

def fetch(self, pc: int, simulation) -> str:
    temp = simulation.i_mem.data[pc: pc+4]
    instruction = ""
    instruction += temp
    FD_intermediate.setValue(instruction)
    return instruction

def decode(self, instruction):
    DX_intermediates['opcode'].setValue(FD_intermediate[0:7])  # opcode
    DX_intermediates['rd'].setValue(FD_intermediate[7:12]) # rd
    DX_intermediates['func3'].setValue(FD_intermediate[12:15]) # func3
    DX_intermediates['rs1'].setValue(FD_intermediate[15:20]) # rs1
    DX_intermediates['rs2'].setValue(FD_intermediate[20:25]) # rs2
    DX_intermediates['func7'].setValue(FD_intermediate[25::]) # func7
    

def execute():
    pass

def memory():
    pass

def writeback():
    pass
