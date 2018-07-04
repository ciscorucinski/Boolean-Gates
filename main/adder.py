from main.logic_gates.basic import and_gate, or_gate
from main.logic_gates.composite import xor_gate

carry = 0
sum = 1


def half_adder(a, b):
    return and_gate(a, b), xor_gate(a, b)


def full_adder(a, b, c):
    half1 = half_adder(a, b)
    half2 = half_adder(half1[sum], c)

    return or_gate(half1[carry], half2[carry]), half2[sum]


def adder_8bit(a, b):
    add0 = half_adder(a[7], b[7])
    add1 = full_adder(a[6], b[6], add0[carry])
    add2 = full_adder(a[5], b[5], add1[carry])
    add3 = full_adder(a[4], b[4], add2[carry])
    add4 = full_adder(a[3], b[3], add3[carry])
    add5 = full_adder(a[2], b[2], add4[carry])
    add6 = full_adder(a[1], b[1], add5[carry])
    add7 = full_adder(a[0], b[0], add6[carry])

    if add7[carry] == 1:
        raise OverflowError

    value = (add7[sum], add6[sum], add5[sum], add4[sum], add3[sum], add2[sum], add1[sum], add0[sum])

    return value


def subtracter_8bit(a, b):
    print("Subtract results")
    # return adder_8bit(a, tuple(not_gate(x) for x in b))
