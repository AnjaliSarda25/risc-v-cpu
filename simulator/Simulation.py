import simulator.components as comp

MEM_DELAY_CYCLES = 1

class Simulation:

    def __init__(self, 
    binary: str, no_of_instructions: int, 
    i_mem_delay: int = MEM_DELAY_CYCLES, 
    d_mem_delay: int = MEM_DELAY_CYCLES) -> None:

        '''Creates instances of InstructionMemory, DataMemory and CPU and initializes with their required parameters'''
        
        print("Simulator initialized")
        self.i_mem = comp.InstructionMemory(binary, i_mem_delay)
        print(self.i_mem)
        self.d_mem = comp.DataMemory(d_mem_delay)
        self.cpu = comp.CPU(no_of_instructions, self.i_mem, self.d_mem)

    def begin(self):
        print("Simulation has begun")
        self.cpu.run()
        


    
