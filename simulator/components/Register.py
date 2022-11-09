SIGNED_CEIL = 2 ** 31
UNSIGNED_CEIL = 2 ** 32

class Register:

    def __init__(self, size: int = 32) -> None:
        self.size = size
        self.value = '0' * size
        self.available = True
    
    def getValue(self) -> int:
        val = int(self.value, 2)
        if val >= SIGNED_CEIL:
            return val - UNSIGNED_CEIL
        return val
    
    def setValue(self, val) -> None:    
        if val < 0:
            val = val + UNSIGNED_CEIL
        bin_val = bin(val)[2:]
        zero_bits = '0' * (self.size - len(bin_val))
        self.value = zero_bits + bin_val

    def toggleAvailability(self) -> None:
        self.available = not self.available