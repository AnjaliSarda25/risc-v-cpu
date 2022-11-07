from simulator.components.Pipeline import fetch, decode, execute, memory, writeback
from simulator.components.Register import Register

FD_intermediate = str()

DX_intermediates = {
    'rs1_data' : Register(),
    'rs2_data' : Register(),
    'imm' : Register(12),
    'rd' : str(),
    'funct10' : str()  
    }

XM_intermediates = {
    'res_data' : Register(),
    'rd' : str(),
    'operation_name' : str()
    }

MW_intermediate = Register()

class CtrlUnit:
    
    def __init__(self):
        print("CU created")

    def pipeline(self, reg_file, i_mem, d_mem):
        pass

        
