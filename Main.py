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
input_file = open("test_binary", "r")

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

for i, state in enumerate(reg_states):
    output_file.write("## Cycle: {}\n---\n".format(i))
    
    output_file.write("| ")
    
    r = range(len(state))

    for j in r:
        output_file.write("x[{}] | ".format(j))

    output_file.write("\n|")
    
    for k in r:
        output_file.write("-|")

    output_file.write("\n| ")
    
    for l in r:
        output_file.write("{} | ".format(state[l]))
    
    output_file.write("\n\n")