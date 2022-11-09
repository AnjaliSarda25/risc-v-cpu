import simulator.components as comp

NO_OF_REGISTERS = 32

class RegisterFile:

    def __init__(self) -> None:
        '''
        Initialize 32 general purpose registers and the program counter
        '''
        print("RegisterFile created")
        self.program_counter = comp.Register()
        self.gen_registers = []

        i = 0
        while (i != NO_OF_REGISTERS):
            self.gen_registers.append(comp.Register())
            i += 1
        
    def getState(self):
        reg_values = []

        for reg in self.gen_registers:
            reg_values.append(reg.getValue())
        
        reg_values.append(self.program_counter.getValue())
        return reg_values