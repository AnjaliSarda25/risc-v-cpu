class ALU:
    def __init__(self):
        print("ALU created")
        pass

    def ADD(self, rs1, rs2):
        return rs1 + rs2 
    
    def SUB(self, rs1, rs2):
        return rs1 - rs2 
    
    def MUL(self, rs1, rs2):
        return rs1 * rs2 
    
    def OR(self, rs1, rs2):
        return rs1 | rs2 
    
    def AND(self, rs1, rs2):
        return rs1 & rs2

    def SLL(self, rs1):
        '''Returns the result of applying a logical left shift to input value'''
        pass

    def SRA(self, rs1):
        '''Returns the result of applying an arithmetic right shift to input value'''
        pass

    def getOperation(self, opcode):
        '''Returns the corresponding operation function for input opcode'''
        pass



        
        
