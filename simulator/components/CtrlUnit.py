from simulator.components.Pipeline import fetch, decode, execute, memory, writeback
from simulator.components.Register import Register

instruction_memory: object
data_memory: object
ALU: object

class CtrlUnit:
    
    def __init__(self, i_mem, d_mem):
        print("CU created")
        instruction_memory = i_mem
        print(instruction_memory)
        data_memory = d_mem


    def pipeline(self):
        pass

    