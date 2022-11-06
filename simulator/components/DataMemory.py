from simulator.components.Memory import Memory

MEM_SIZE = 16384 + 5*4

class DataMemory(Memory):

    def __init__(self, size: int = MEM_SIZE) -> None:
        print("DMem created")
        pass

    def setData(self, address: int, newVal: int) -> None:
        '''
        Function to update the data present at the (address)th index of the memory
        '''
        pass