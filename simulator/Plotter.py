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
    plt.tight_layout()
    plt.gcf().set_size_inches(15, 5)
    plt.savefig("imem.jpg", dpi=1000)

def plotDMemAccesses(cpu_states):
    cycles = list()
    d_mem_access = list()

    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['pipelined'][i][3] and cpu_states['pipelined'][i][3] in cpu_states['mem_instructions']:
            cycles.append(i)
            addr = cpu_states['mem_accesses'][i - 1]
            d_mem_access.append(addr)
    
    print(cycles)
    print(d_mem_access)

    fig, ax = plt.subplots()
    ax.scatter(cycles, d_mem_access, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Data Address")
    plt.title("Data Memory Access Pattern")
    plt.xticks(cycles)
    plt.yticks(d_mem_access)
    plt.tight_layout()
    plt.gcf().set_size_inches(15, 5)
    plt.savefig("dmem.jpg", dpi=1000)

def plotStalls(cpu_states):
    cycles = list()
    stage = list()
    stages = ["Fetch", "Decode", "Execute", "Memory", "Writeback", "No stall"]
    
    fig, ax = plt.subplots()

    for i in range(len(cpu_states['reg_values'])): 
        cycles.append(i)
        if cpu_states['stalled'][i][0]:
            stage.append("Fetch")
        elif cpu_states['stalled'][i][1]:
            stage.append("Decode")
        elif cpu_states['stalled'][i][2]:
            stage.append("Execute")
        elif cpu_states['stalled'][i][3]:
            stage.append("Memory")
        elif cpu_states['stalled'][i][4]:
            stage.append("Writeback")
        else:
            stage.append("No stall")    
    
    ax.scatter(cycles, stage, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Stage")
    plt.title("Stalls vs Cycles")
    plt.xticks(cycles)
    plt.tight_layout()
    plt.gcf().set_size_inches(15, 5)
    plt.savefig("stalls.jpg", dpi=1000)
    