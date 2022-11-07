from simulator.components.Register import Register

NO_OF_REGISTERS = 32

class RegisterFile:

    # registers = list()

    def __init__(self) -> None:
        '''
        Initialize 32 general purpose registers and the program counter
        '''
        print("RegisterFile created")
        self.program_counter = Register()
        self.gen_registers = []

        i = 0
        while (i != NO_OF_REGISTERS):
            self.gen_registers.append(Register())
            i += 1