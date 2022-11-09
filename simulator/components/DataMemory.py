from simulator.components.Memory import Memory

MEM_SIZE = 16384 + 5*4
UNSIGNED_CEIL = 2 ** 32

class DataMemory(Memory):

    def __init__(self, delay: int, size: int = MEM_SIZE) -> None:
        print("DMem created")
        super().__init__(size, delay)
        pass

    def writeData(self, address: int, data: int) -> bool:
        '''
        Writes input data to the given address after number of cycles as given by the data memory's delay property, and returns True.\n
        Returns False if a new request is made or a request is currently being processed.
        '''
        if (self.res_time == -1):
            self.res_time = self.delay

        if (self.res_time == 0):
            if data < 0:
                data = data + UNSIGNED_CEIL
            
            bin_data = bin(data)[2:]
            zero_bits = '0' * (32 - len(bin_data))
            data_str = zero_bits + bin_data
            
            self.data[address]      = data_str[:8]
            self.data[address + 1]  = data_str[8:16]
            self.data[address + 2]  = data_str[16:24]
            self.data[address + 3]  = data_str[24:]
            return True
        
        return False