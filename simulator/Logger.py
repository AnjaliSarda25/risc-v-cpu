import sys

sys.path.append("../")
log_file = open("log.txt", "w")

def generateLog(d_mem_state, cpu_states):
    stages = ["Fetch", "Decode", "Execute", "Memory", "Writeback"]
    for i in range(len(cpu_states['reg_values'])):
        
        head = "At the end of cycle {}\n\n".format(i)
        log_file.write(head)

        for j in range(len(cpu_states['reg_values'][i]) - 1):
            
            line = "r{}: {}\n".format(j, cpu_states['reg_values'][i][j])
            log_file.write(line)

        line = "pc: {}\n".format(cpu_states['reg_values'][i][32])
        log_file.write(line)

        log_file.write("\n")
        for k in range(len(stages)):
            log_file.write("Stage: ")
            log_file.write(stages[k])
            log_file.write("\n")
            log_file.write("Instruction in stage: ")
            log_file.write(str(cpu_states['pipelined'][i][k]))
            log_file.write("\n")
            log_file.write("Stalled: ")
            log_file.write(str(cpu_states['stalled'][i][k]))
            log_file.write("\n")
            log_file.write("\n")
        
        log_file.write("\n")

def summarizeLog():
    pass

