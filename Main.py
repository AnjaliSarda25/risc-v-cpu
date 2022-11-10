import simulator
import argparse

INSTRUCTION_SIZE = 32
MEM_DELAY_CYCLES = 0

parser = argparse.ArgumentParser()

parser.add_argument('--ddelay', help="Sets the delay cycles for data memory")
parser.add_argument('--idelay', help="Sets the delay cycles for instruction memory")

args = parser.parse_args()

if not args.ddelay:
    args.ddelay = MEM_DELAY_CYCLES
if not args.idelay:
    args.idelay = MEM_DELAY_CYCLES

input_binary = ""

# Open file containing the test binary
input_file = open("test_bin", "r")

# Store contents of input_file as a string
file_content = input_file.read()

# Split file_content separated by whitespaces and store as a list
content_list = file_content.split()

# Join all strings of the list
input_binary = input_binary.join(content_list)

# input_binary stores the test binary without any whitespace separating the content

no_of_instructions = len(input_binary) / INSTRUCTION_SIZE

# Run the simulation
simulation = simulator.Simulation(input_binary, no_of_instructions, args.idelay, args.ddelay)
simulation.begin()

# Generating log file
reg_states = simulation.getPerCycleRegState()
final_mem_state = simulation.getFinalDMemState()

output_file = open("log.md", "w")

output_file.write("# Log File:\n\n")

output_file.write("## Total number of cycles = {}\n\n\n".format(len(reg_states) - 1))
output_file.write("<br>\n\n")

for i, state in enumerate(reg_states):
    output_file.write("### State of register file when cycles passed = {}\n---\n".format(i))
    
    output_file.write("| ")
    
    r = range(len(state))

    for j in r:
        if j == 32:
            output_file.write("pc | ")
        else:    
            output_file.write("x[{}] | ".format(j))

    output_file.write("\n|")
    
    for k in r:
        output_file.write("-|")

    output_file.write("\n| ")
    
    for l in r:
        output_file.write("{} | ".format(state[l]))
    
    output_file.write("\n\n")

output_file.write("<br>")
output_file.write("<br>\n\n")
output_file.write("## State of Memory Mapped Registers and the end of program: \n")
output_file.write("```\n")
output_file.write("- 0x4000: {}\n".format(simulation.d_mem.readData(16384)))
output_file.write("- 0x4004: {}\n".format(simulation.d_mem.readData(16388)))
output_file.write("- 0x4008: {}\n".format(simulation.d_mem.readData(16392)))
output_file.write("- 0x400c: {}\n".format(simulation.d_mem.readData(16396)))
output_file.write("- 0x4010: {}\n".format(simulation.d_mem.readData(16400)))
output_file.write("```\n")

output_file.write("<br>")
output_file.write("<br>\n\n")
output_file.write("## State of Data Memory at the end of program: \n")
output_file.write("```\n")

for i in range(16384):
    output_file.write("- D_Mem[{}]:     {}\n".format(i, simulation.d_mem.data[i]))
output_file.write("```\n")