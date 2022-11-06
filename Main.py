import simulator

input_binary = ""
INSTRUCTION_SIZE = 32

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
simulation = simulator.Simulation(input_binary, no_of_instructions)
simulation.begin()
