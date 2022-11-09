import simulator.components as comp

class CtrlUnit:
    
    def __init__(self):
        print("CU created")

    def pipeline(self, reg_file: comp.RegisterFile, i_mem: comp.InstructionMemory, d_mem: comp.DataMemory):
        state = {}
        
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
            comp.FD_intermediate.clear()

        state['f'] = comp.fetch(reg_file)
        
        return state

    def flush():
        comp.FD_intermediate = ""
        comp.DX_intermediate.clear()
        comp.XM_intermediate.clear()
        comp.MW_intermediate.clear()