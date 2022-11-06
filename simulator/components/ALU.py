class ALU:
    def __init__(self):
        print("ALU created")
        pass

    def ADD(rs1, rs2):
        return rs1 + rs2 
    
    def SUB(rs1, rs2):
        return rs1 - rs2 
    
    def MUL(rs1, rs2):
        return rs1 * rs2 
    
    def OR(rs1, rs2):
        return rs1 or rs2 
    
    def AND(rs1, rs2):
        return rs1 and rs2

    def SLL(rs1):
        '''Returns the result of applying a logical left shift to input value'''
        pass

    def SRA(rs1):
        '''Returns the result of applying an arithmetic right shift to input value'''
        pass

    def getOperation(self, opcode):
        '''Returns the corresponding operation function for input opcode'''
        pass



        
        
