MAX_VAL = 2 ** 32 - 1

def ADD(in_1, in_2):
    '''Returns the sum of input values'''
    return (in_1 + in_2) % MAX_VAL

def SUB(in_1, in_2):
    '''Returns the difference of input values'''
    return (in_2 - in_1) % MAX_VAL

def OR(in_1, in_2):
    '''Returns the bitwise OR of input values'''
    return in_1 | in_2 

def AND(in_1, in_2):
    '''Returns the bitwise AND of input values'''
    return in_1 & in_2

def SLL(in_1, in_2):
    '''Returns the result of applying logical left shift to in_1, in_2 number of times'''
    pass

def SRA(in_1, in_2):
    '''Returns the result of applying logical left shift to in_1, in_2 number of times'''
    pass

def getResult(rs1_data, rs2_data, funct):
    alu_dict = {''}