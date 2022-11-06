from simulator.components.Register import Register

# Store fetched instruction
FD_intermediate = Register()

# Store decoded parts of fetched instruction in respective fields
DX_intermediates = {
    'opcode':Register(), 
    'rs1':Register(), 
    'rs2':Register(), 
    'imm':Register(), 
    'rd':Register(),
    'mem_addr':Register()
    }

XM_intermediates = {
    'mem_addr':Register(),
    'rd':Register()
    }

# Store address of register here
MW_intermediate = Register()

def fetch(self, pc: int, simulation) -> str:
    pass

def decode():
    pass

def execute():
    pass

def memory():
    pass

def writeback():
    pass
