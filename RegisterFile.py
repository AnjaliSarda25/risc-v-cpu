from Register import Register

class RegisterFile:

    registers = list()

    def __init__(self, size: int) -> None:
        '''
        Construtor is used to initialize the list of registers to a specific sized list of objects of the Register class  
        '''
        pass

    def setRegister(self, registerName: str, value: int) -> None:
        '''
        Sets the value of the register with the name "registerName" in the list of registers to the value contained in "value"
        '''
        pass

    def getRegister(self, registerName: str) -> int:
        '''
        Gets the value of the register with the name "registerName" in the list of registers
        '''
        pass