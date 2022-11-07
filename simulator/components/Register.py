XLEN = 32

class Register:

    def __init__(self, size: int = XLEN) -> None:
        self.size = size
        self.value = '0' * size
        self.available = True
    
    def getValue(self) -> int:
        return int(self.value, 2)
    
    def setValue(self, val) -> None:    
        bin_val = bin(val)[2:]
        zero_bits = '0' * (self.size - len(bin_val))
        self.value = zero_bits + bin_val

    def toggleAvailability(self) -> None:
        self.available = not self.available
