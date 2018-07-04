from main.adder import adder_8bit, subtracter_8bit
from main.utility import bits_4


def alu_execute(a, b, opcode):
    if opcode == bits_4(8):
        return adder_8bit(a, b)
    elif opcode == bits_4(12):
        return subtracter_8bit(a, b)
    else:
        pass
