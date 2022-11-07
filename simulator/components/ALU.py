CEIL = (2 ** 31)
MAX = (2 ** 31) - 1
MIN = -(2 ** 32)

def resolveOverflow(val: int) -> int:
    '''Returns the mod CEIL value if the computed value is out of range'''
    if (val > MAX or val < MIN):
        return val % CEIL

def ADD(in_1: int, in_2: int) -> int:
    '''Returns the sum of input values'''
    sum = in_1 + in_2
    sum = resolveOverflow(sum)
    return sum

def SUB(in_1: int, in_2: int) -> int:
    '''Returns the difference of input values'''
    diff = in_2 - in_1
    diff = resolveOverflow(diff)
    return diff

def OR(in_1: int, in_2: int) -> int:
    '''Returns the bitwise OR of input values'''
    return in_1 | in_2 

def AND(in_1: int, in_2: int) -> int:
    '''Returns the bitwise AND of input values'''
    return in_1 & in_2

def SLL(in_1: int, in_2: int) -> int:
    '''
    Returns the result of applying logical left shift to in_1, in_2 % 32 number of times
    in_2 % 32 corresponds to the value given by least 5 bits of in_2
    '''
    shift = in_2 % 32
    res = in_1 << shift
    res = resolveOverflow(res)
    return res

def SRA(in_1: int, in_2: int) -> int:
    '''
    Returns the result of applying arithmetic right shift to in_1, in_2 % 32 number of times
    in_2 % 32 corresponds to the value given by least 5 bits of in_2
    '''
    shift = in_2 % 32
    return in_1 >> shift

def getResult(in_1: int, in_2: int, funct: str) -> int:
    '''Maps funct bits to the function of the operation they represent'''
    alu_dict = {
        '0000000000' : ADD,
        '0100000000' : SUB,
        '0000000001' : SLL,
        '0100000101' : SRA,
        '0000000110' : OR,
        '0000000111' : AND
        }
    
    return alu_dict[funct](in_1, in_2)