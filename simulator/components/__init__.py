from simulator.components.Register import Register
from simulator.components.RegisterFile import RegisterFile
from simulator.components.InstructionMemory import InstructionMemory
from simulator.components.DataMemory import DataMemory
from simulator.components.CtrlUnit import CtrlUnit
from simulator.components.CPU import CPU
from simulator.components.ALU import getResult
from simulator.components.Commons import FD_intermediate, DX_intermediate, XM_intermediate, MW_intermediate, BEQ_instructions
from simulator.components.Pipeline import fetch, decode, execute, memory, writeback