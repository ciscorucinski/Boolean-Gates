from component.logic_gates.basic import and_gate, or_gate, not_gate
from utility.alias import Bit


def nand_gate(a: Bit, b: Bit) -> Bit:
    return not_gate(and_gate(a, b))


def nor_gate(a: Bit, b: Bit) -> Bit:
    return not_gate(or_gate(a, b))


def xor_gate(a: Bit, b: Bit) -> Bit:
    return and_gate(nand_gate(a, b), or_gate(a, b))
