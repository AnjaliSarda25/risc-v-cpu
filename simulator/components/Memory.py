class Memory:

    def __init__(self, size: int, delay: int) -> None:
        '''
        Initializes the memory to be of a fixed size
        '''
        self.data = ["00000000",] * size

    def getData(self, address: int) -> str:
        '''
        Function to return the data present at the (address)th index of the memory
        '''
        pass