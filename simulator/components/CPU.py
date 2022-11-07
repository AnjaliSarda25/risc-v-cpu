import simulator.components as comp

class CPU:
    def __init__(self, no_of_instructions, i_mem, d_mem):
        print("CPU created")
        self.register_file = comp.RegisterFile()
        self.ctrl_unit = comp.CtrlUnit()
        self.no_of_instructions = no_of_instructions
        self.cycles = 0

    def run(self):
        pass

        

