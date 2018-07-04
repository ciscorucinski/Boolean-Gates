from typing import NamedTuple, Tuple
import attr

Bit = int
#Byte = Tuple[Bit, Bit, Bit, Bit, Bit, Bit, Bit, Bit]
# Nibble = Tuple[Bit, Bit, Bit, Bit]

@attr.s
class Byte(object): #NamedTuple("Byte", bit8=Bit, bit7=Bit, bit6=Bit, bit5=Bit, bit4=Bit, bit3=Bit, bit2=Bit, bit1=Bit)):

    bit8 = attr.ib()
    bit7 = attr.ib()
    bit6 = attr.ib()
    bit5 = attr.ib()
    bit4 = attr.ib()
    bit3 = attr.ib()
    bit2 = attr.ib()
    bit1 = attr.ib()

    def __iter__(self):
        yield self.bit8
        yield self.bit7
        yield self.bit6
        yield self.bit5
        yield self.bit4
        yield self.bit3
        yield self.bit2
        yield self.bit1


class Nibble(NamedTuple("Byte", bit4=Bit, bit3=Bit, bit2=Bit, bit1=Bit)):
    pass


class Adder(NamedTuple("Adder", sum=Bit, carry=Bit)):
    pass
