from utility.alias import Byte
from utility.byte_utility import byte, byte_tuple, negate_byte

tuple_zero = (0, 0, 0, 0, 0, 0, 0, 0)
tuple_one = (0, 0, 0, 0, 0, 0, 0, 1)
tuple_170 = (1, 0, 1, 0, 1, 0, 1, 0)
tuple_209 = (1, 1, 0, 1, 0, 0, 0, 1)
tuple_255 = (1, 1, 1, 1, 1, 1, 1, 1)

byte_0 = Byte(*tuple_zero)
byte_1 = Byte(*tuple_one)
byte_255 = Byte(*tuple_255)
byte_170 = Byte(*tuple_170)
byte_209 = Byte(*tuple_209)

print("Verified Byte Utilities")

assert byte_0.bit1 == 0
assert byte_0.bit2 == 0
assert byte_0.bit3 == 0
assert byte_0.bit4 == 0
assert byte_0.bit5 == 0
assert byte_0.bit6 == 0
assert byte_0.bit7 == 0
assert byte_0.bit8 == 0

assert byte_209.bit1 == 1
assert byte_209.bit2 == 0
assert byte_209.bit3 == 0
assert byte_209.bit4 == 0
assert byte_209.bit5 == 1
assert byte_209.bit6 == 0
assert byte_209.bit7 == 1
assert byte_209.bit8 == 1

assert byte_170.bit1 == 0
assert byte_170.bit2 == 1
assert byte_170.bit3 == 0
assert byte_170.bit4 == 1
assert byte_170.bit5 == 0
assert byte_170.bit6 == 1
assert byte_170.bit7 == 0
assert byte_170.bit8 == 1

assert byte_255.bit1 == 1
assert byte_255.bit2 == 1
assert byte_255.bit3 == 1
assert byte_255.bit4 == 1
assert byte_255.bit5 == 1
assert byte_255.bit6 == 1
assert byte_255.bit7 == 1
assert byte_255.bit8 == 1
print("\t- Check each bit in Byte type alias is correct")

# Checking Byte Type Alias is stored as a Tuple of 8 items
assert (byte_0.bit8, byte_0.bit7, byte_0.bit6, byte_0.bit5,
        byte_0.bit4, byte_0.bit3, byte_0.bit2, byte_0.bit1) == tuple_zero     # Tuple[int x8]
print("\t- Byte type alias stored as Tuple with 8 ints")

# Checking equality to Byte type alias
assert byte(0) == byte_0        # Byte(...)
assert byte(1) == byte_1
assert byte(255) == byte_255
assert byte(170) == byte_170
assert byte(209) == byte_209
print("\t- byte function == Byte type alias")


assert byte(256) == byte(0) == byte_0
assert byte(256 + 170) == byte_170
print("\t- overflowing byte function is down-casted to 1 byte")

assert byte_tuple("00000000") == byte_0
assert byte_tuple("00000001") == byte_1
assert byte_tuple("10101010") == byte_170
assert byte_tuple("11010001") == byte_209
assert byte_tuple("11111111") == byte_255
print("\t- Byte String to Byte Tuple function")


assert negate_byte(byte_tuple("00000000")) == byte_tuple("11111111")

