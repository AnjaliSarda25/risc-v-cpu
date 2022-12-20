from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

def plotIMemAccesses(cpu_states):
    cycles = list()
    i_mem_access = list()

    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['pipelined'][i][0]:
            cycles.append(i)
            addr = (cpu_states['pipelined'][i][0] - 1) * 4
            i_mem_access.append(addr)
    
    print(cycles)
    print(i_mem_access)

    fig, ax = plt.subplots()

    ax.scatter(cycles, i_mem_access, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Instruction Address")
    plt.title("Instruction Memory Access Pattern")
    plt.xticks(cycles)
    plt.yticks(i_mem_access)
    plt.gcf().set_size_inches(20, 7)
    plt.tight_layout()
    plt.savefig("imem.jpg", dpi=1000)

def plotDMemAccesses(cpu_states):
    cycles = list()
    d_mem_access = list()

    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['pipelined'][i][3] and cpu_states['pipelined'][i][3] in cpu_states['mem_instructions']:
            cycles.append(str(i))
            addr = cpu_states['mem_accesses'][i - 1]
            d_mem_access.append(str(addr))
    
    print(cycles)
    print(d_mem_access)

    fig, ax = plt.subplots()
    ax.scatter(cycles, d_mem_access, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Data Address")
    plt.title("Data Memory Access Pattern")
    plt.xticks(cycles)
    plt.yticks(d_mem_access)
    plt.gcf().set_size_inches(20, 7)
    plt.tight_layout()
    plt.savefig("dmem.jpg", dpi=1000)

def plotStalls(cpu_states):
    cycles = list()
    stage = list()
    stages = ["Fetch", "Decode", "Execute", "Memory", "Writeback", "No stall"]
    
    fig, ax = plt.subplots()

    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['stalled'][i][0]:
            cycles.append(i)
            stage.append("Fetch")
        if cpu_states['stalled'][i][1]:
            cycles.append(i)
            stage.append("Decode")
        if cpu_states['stalled'][i][2]:
            cycles.append(i)
            stage.append("Execute")
        if cpu_states['stalled'][i][3]:
            cycles.append(i)
            stage.append("Memory")
        if cpu_states['stalled'][i][4]:
            cycles.append(i)
            stage.append("Writeback")
        if not(cpu_states['stalled'][i][0] or cpu_states['stalled'][i][1] or cpu_states['stalled'][i][2] or cpu_states['stalled'][i][3] or cpu_states['stalled'][i][4]):
            cycles.append(i)
            stage.append("No stall")    
    
    ax.scatter(cycles, stage, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Stage")
    plt.title("Stalls vs Cycles")
    plt.xticks(cycles)
    plt.gcf().set_size_inches(20, 7)
    plt.tight_layout()
    plt.savefig("stalls.jpg", dpi=1000)
    