# Cycle accurate simulator for 5-stage pipelined RISC-V CPU

This project simulates a 5-stage pipelined CPU executing a binary encoded in the RV32I variant of the RISC-V ISA.

Instructions supported:

ISA instructions:

- ADD rd rs1 rs2
- SUB rd rs1 rs2
- AND rd rs1 rs2
- OR rd rs1 rs2
- SLL rd rs1 rs2
- SRA rd rs1 rs2
- LW rd rs1 off
- SW rs2 rs1 off
- BEQ rs2 rs1 off

Additional instructions:

- LOADNOC rs2 rs1 off
- STORENOC

Current Features:

1. Simulator is able to parse all instructions given as an input binary and simulate their pipelined execution
2. Supports decode stalling in case of read after write data dependencies
3. Generates log file recording the total number of cycles, the state of the register file per clock cycle and the state of the data memory and memory mapped registers at the end of the simulation.

<hr>

## Steps to run:

1. Clone the repository
2. cd into top level directory
3. run `python3 Main.py`

<hr>

## Please See: Assumptions

As stated in the specifications of the RISC-V ISA,

1. the endianness of memory systems can be either little or big endian - it depends on the execution environment. We assume our data and instruction memory store data in big endian format.

2. an exception must be raised if a branch instruction's target address wil result in a misaligned instruction memory access. We assume that this exception simply skips over the instruction that generates it and the simulation continues. The cycle at which the exception is raised is logged to the log file.

3. it is up to the execution environment to allow misaligned data memory accesses by load and store operations. We assume that our data memory allows for misaligned memory access.


Further assumptions:

- In case both the writeback and the decode stage try to access the same register of the register file in the same cycle, the writeback stage will complete the write first and toggle the availability of the register it wrote to, making it available for access by the decode stage next in the same cycle.

- the BEQ operation is completed during it's execute phase, after which the pipeline is flushed.
