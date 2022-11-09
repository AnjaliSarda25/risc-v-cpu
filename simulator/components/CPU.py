import simulator.components as comp

class CPU:
    def __init__(self, no_of_instructions):
        print("CPU created")
        self.reg_file = comp.RegisterFile()
        self.ctrl_unit = comp.CtrlUnit()
        self.no_of_instructions = no_of_instructions
        self.cycles = 0

    def run(self, i_mem, d_mem):
        i = 1
        while (i <= self.no_of_instructions):
            self.cycles += 1
            state = self.ctrl_unit.pipeline(self.reg_file, i_mem, d_mem)
            
            if state['w']:
                i += 1

            if type(state['x']) is int:
                self.ctrl_unit.flush()
                self.reg_file.program_counter = state['x']
                continue
            
            if state['f']:
                self.reg_file.program_counter += 4