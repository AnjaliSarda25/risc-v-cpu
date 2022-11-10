import simulator.components as comp

class Simulation:

    def __init__(self, 
    binary: str, 
    no_of_instructions: int,
    i_mem_delay: int, 
    d_mem_delay: int) -> None:
        
        self.i_mem = comp.InstructionMemory(binary, i_mem_delay)
        print(self.i_mem)
        self.d_mem = comp.DataMemory(d_mem_delay)
        self.cpu = comp.CPU(no_of_instructions)
        self.reg_values = None

    def begin(self):
        print("- simulation has begun!")
        self.reg_values = self.cpu.run(self.i_mem, self.d_mem)

    def getPerCycleRegState(self):
        return self.reg_values
    
    def getFinalDMemState(self):
        return self.d_mem.data