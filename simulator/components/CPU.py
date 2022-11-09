import simulator.components as comp

class CPU:
    def __init__(self, no_of_instructions):
        print("CPU created")
        self.reg_file = comp.RegisterFile()
        self.ctrl_unit = comp.CtrlUnit()
        self.no_of_instructions = no_of_instructions
        self.cycles = 0

    def run(self, i_mem: comp.InstructionMemory, d_mem: comp.DataMemory):
        '''
        Loops pipelined execution of instructions until all instructions are executed.\n
        Returns the per cycle register state of the program as a list of lists.
        '''

        i = 1
        reg_values = []
        
        while (i <= self.no_of_instructions):
            reg_values.append(self.reg_file.getState())
            
            self.cycles += 1
            i_mem.decrementResTime()
            d_mem.decrementResTime()
            
            state = self.ctrl_unit.pipeline(self.reg_file, i_mem, d_mem, self.no_of_instructions)
            
            if state['w']:
                i += 1

            if type(state['x']) is int:
                self.ctrl_unit.flush()
                self.reg_file.program_counter.setValue(state['x'])

                if (self.reg_file.program_counter.getValue() % 4) != 0:
                    print("Exception: Misaligned Instruction Memory Access")
                    break
                
                jump = state['x'] / 4
                i += jump
                continue
            
            if state['f']:
                pc = self.reg_file.program_counter.getValue()
                pc += 4
                self.reg_file.program_counter.setValue(pc)
        
        reg_values.append(self.reg_file.getState())
        return reg_values