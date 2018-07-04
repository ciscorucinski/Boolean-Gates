from main.ALU import alu_execute
from main.adder import half_adder, full_adder, adder_8bit
from main.logic_gates.basic import and_gate, or_gate, not_gate
from main.logic_gates.composite import xor_gate
from main.op_code import add, sub
from main.utility import bits_8

print()

print("Verifying And Gates...")
assert and_gate(0, 0) == 0
assert and_gate(0, 1) == 0
assert and_gate(1, 0) == 0
assert and_gate(1, 1) == 1
print("\tAnd Gates are all correct!")
print()

print("Verifying Or Gates...")
assert or_gate(0, 0) == 0
assert or_gate(0, 1) == 1
assert or_gate(1, 0) == 1
assert or_gate(1, 1) == 1
print("\tOr Gates are all correct!")
print()

print("Verifying Not Gates...")
assert not_gate(0) == 1
assert not_gate(1) == 0
print("\tNot Gates are all correct!")
print()

print("Verifying Xor Gates...")
assert xor_gate(0, 0) == 0
assert xor_gate(0, 1) == 1
assert xor_gate(1, 0) == 1
assert xor_gate(1, 1) == 0
print("\tXor Gates are all correct!")
print()

print("Verifying Half Adder")
assert half_adder(0, 0) == (0, 0)
assert half_adder(0, 1) == (0, 1)
assert half_adder(1, 0) == (0, 1)
assert half_adder(1, 1) == (1, 0)
print("\tHalf Adder is all correct!")
print()

print("Verifying Full Adder")
assert full_adder(0, 0, 0) == (0, 0)
assert full_adder(0, 0, 1) == (0, 1)
assert full_adder(0, 1, 0) == (0, 1)
assert full_adder(0, 1, 1) == (1, 0)
assert full_adder(1, 0, 0) == (0, 1)
assert full_adder(1, 0, 1) == (1, 0)
assert full_adder(1, 1, 0) == (1, 0)
assert full_adder(1, 1, 1) == (1, 1)
print("\tFull Adder is all correct!")
print()

print("Verifying 8-bit Adder")
assert adder_8bit(bits_8(0), bits_8(0)) == bits_8(0)
assert adder_8bit(bits_8(0), bits_8(1)) == bits_8(1)
assert adder_8bit(bits_8(1), bits_8(1)) == bits_8(2)
assert adder_8bit(bits_8(0), bits_8(255)) == bits_8(255)
assert adder_8bit(bits_8(127), bits_8(127)) == bits_8(254)
assert adder_8bit(bits_8(21), bits_8(78)) == bits_8(99)
assert adder_8bit(bits_8(254), bits_8(1)) == bits_8(255)

try:
    assert adder_8bit(bits_8(255), bits_8(1))
except OverflowError:
    pass

try:
    assert adder_8bit(bits_8(255), bits_8(255))
except OverflowError:
    pass

print("\t8-bit Adder is all correct!")
print()

# print("Verifying 8-bit Subtracter")
# assert subtracter_8bit(bits_8(0), bits_8(0)) == bits_8(0)
# assert subtracter_8bit(bits_8(1), bits_8(0)) == bits_8(1)
# assert subtracter_8bit(bits_8(1), bits_8(1)) == bits_8(2)
# print("\t8-bit Subtracter is all correct!")
# print()

print("Verifying ALU")
assert alu_execute(bits_8(127), bits_8(127), add) == bits_8(254)
assert alu_execute(bits_8(8), bits_8(2), sub) == bits_8(6)
print("\tALU is all correct!")
print()
