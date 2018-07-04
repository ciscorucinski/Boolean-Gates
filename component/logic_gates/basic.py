from component.transistor import transistor_internals
from utility.alias import Bit


def and_gate(a: Bit, b: Bit) -> Bit:
    # return transistor_internals(a, 1, 0) and transistor_internals(b, 1, 0)

    # transistor_a = transistor_internals(b, a, 0)
    # transistor_b = transistor_internals(transistor_a, 1, 0)

    return transistor_internals(transistor_internals(a, b, 0), 1, 0)


def or_gate(a: Bit, b: Bit) -> Bit:
    return transistor_internals(a, 1, 0) or transistor_internals(b, 1, 0)


def not_gate(a: Bit) -> Bit:
    # return not transistor_internals(a, 1, 0)
    return transistor_internals(a, 0, 1)
