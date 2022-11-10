import simulator.components as comp

class CtrlUnit:
    
    def __init__(self):
        print("CU created")

    def pipeline(self, reg_file: comp.RegisterFile, i_mem: comp.InstructionMemory, d_mem: comp.DataMemory, no_of_instructions: int, i: int):
        state = {}

        print("\n")

        state['w'] = comp.writeback(reg_file)
        if state['w']:
            comp.MW_intermediate.clear()
        
        state['m'] = comp.memory(d_mem)
        if state['m']:
            comp.XM_intermediate.clear()

        state['x'] = comp.execute()
        if state['x']:
            comp.DX_intermediate.clear()
        
        state['d'] = comp.decode(reg_file)
        if state['d']:
            comp.FD_intermediate = ""
 
        state['f'] = comp.fetch(reg_file, i_mem, no_of_instructions, i)
        
        return state

    def flush(self):
        comp.FD_intermediate = ""
        comp.DX_intermediate.clear()
        comp.XM_intermediate.clear()
        comp.MW_intermediate.clear()