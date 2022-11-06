class Register:
    # name = ""       # Name of the register
    # value = 0       # Value the register is holding
    # lock = 0        # Boolean to denote if the register is under use by a previous instruction

    def __init__(self, size: int) -> None:
        self.size = size
        self.value = '0'*size
        self.lock = False
        
        pass

    def getName(self) -> str:
        '''
        Getter function for the name of the register
        '''
        pass

    def toggleState(self) -> None:
        '''
        Function to toggle the current availability or the lock state of the register  
        '''
        pass

    def setValue(self, value: str) -> bool:
        '''
        Setter function for the value parameter.
        \n\t Must ensure that the register is in an unlocked state before updating the value
        \n\t Returns a boolean marking a successful/failed write 
        '''
        pass

    def getValue(self) -> int:
        '''
        Getter function for the value the register is holding
        '''
        pass

    
