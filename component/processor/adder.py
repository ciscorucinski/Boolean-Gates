from component.logic_gates.basic import and_gate, or_gate
from component.logic_gates.composite import xor_gate
from utility.alias import Byte, Bit, Adder


def half_adder(a: Bit, b: Bit) -> Adder:
    """
    Sums two single bits

    :param a: bit 1
    :param b: bit 2
    :return: Returns the sum and carry bits of adding two bits. [0] = sum, [1] = carry
    """
    sum = xor_gate(a, b)
    carry = and_gate(a, b)

    return Adder(sum, carry)


def full_adder(a: Bit, b: Bit, c: Bit) -> Adder:
    """

    :param a: bit 1
    :param b: bit 2
    :param c: bit 3


    :return Returns the sum and carry bits of adding three bits. [0] = sum, [1] = carry
    """
    xor_ab = xor_gate(a, b)

    sum = xor_gate(xor_ab, c)
    carry = or_gate(and_gate(a, b), and_gate(xor_ab, c))

    return Adder(sum, carry)


def adder(byte1: Byte, byte2: Byte) -> Byte:
    """

    :param byte1: byte 1
    :param byte2: byte 2
    :return: Returns the sum of two bytes as a tuple of 8 bits
    """

    # print(byte1.binary)
    add_bits_1 = half_adder(byte1.bit1, byte2.bit1)
    add_bits_2 = full_adder(byte1.bit2, byte2.bit2, add_bits_1.carry)
    add_bits_3 = full_adder(byte1.bit3, byte2.bit3, add_bits_2.carry)
    add_bits_4 = full_adder(byte1.bit4, byte2.bit4, add_bits_3.carry)
    add_bits_5 = full_adder(byte1.bit5, byte2.bit5, add_bits_4.carry)
    add_bits_6 = full_adder(byte1.bit6, byte2.bit6, add_bits_5.carry)
    add_bits_7 = full_adder(byte1.bit7, byte2.bit7, add_bits_6.carry)
    add_bits_8 = full_adder(byte1.bit8, byte2.bit8, add_bits_7.carry)

    value = Byte(bit1=add_bits_1.sum,
                 bit2=add_bits_2.sum,
                 bit3=add_bits_3.sum,
                 bit4=add_bits_4.sum,
                 bit5=add_bits_5.sum,
                 bit6=add_bits_6.sum,
                 bit7=add_bits_7.sum,
                 bit8=add_bits_8.sum
                 )

    if add_bits_8.carry == 1:
        print("8-bit Adder Overflow", byte1, "+", byte2, "=", value)

    print("Sum = " + value.binary)
    return value
