from component.logic_gates.basic import and_gate, or_gate, not_gate
from component.logic_gates.composite import nand_gate, nor_gate, xor_gate
from component.transistor import transistor, transistor_internals

print()

assert transistor(0) == 0
assert transistor(1) == 1
print("Verified Transistor")

assert transistor_internals(0, 1, 0) == 0
assert transistor_internals(1, 1, 0) == 1
print("\t- Direct Transistor")

assert transistor_internals(0, 0, 1) == 1
assert transistor_internals(1, 0, 1) == 0
print("\t- Inverse Transistor")
print()

assert and_gate(0, 0) == 0
assert and_gate(0, 1) == 0
assert and_gate(1, 0) == 0
assert and_gate(1, 1) == 1
print("Verified Gate - And")

assert or_gate(0, 0) == 0
assert or_gate(0, 1) == 1
assert or_gate(1, 0) == 1
assert or_gate(1, 1) == 1
print("Verified Gate - Or")
print()

assert not_gate(0) == 1
assert not_gate(1) == 0
print("Verified Not Gates")
print("\t- Not Gates")

assert nand_gate(0, 0) == 1
assert nand_gate(0, 1) == 1
assert nand_gate(1, 0) == 1
assert nand_gate(1, 1) == 0
print("\t- NAND Gates")

assert nor_gate(0, 0) == 1
assert nor_gate(0, 1) == 0
assert nor_gate(1, 0) == 0
assert nor_gate(1, 1) == 0
print("\t- NOR Gates")
print()

assert xor_gate(0, 0) == 0
assert xor_gate(0, 1) == 1
assert xor_gate(1, 0) == 1
assert xor_gate(1, 1) == 0
print("Verify Xor Gates")
