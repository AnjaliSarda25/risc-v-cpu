import simulator.components as comp

class CPU:
    def __init__(self, no_of_instructions, i_mem, d_mem):
        print("CPU created")
        self.alu = comp.ALU()
        self.ctrl_unit = comp.CtrlUnit(i_mem, d_mem)
        self.register_file = comp.RegisterFile()
        self.cycles = 0

    def run(self):
        pass

        

