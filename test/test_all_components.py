from component.processor.adder import half_adder, full_adder, adder
from utility.byte_utility import byte, byte_tuple

#                    sum <--.  .--> carry
#                           |  |
assert half_adder(0, 0) == (0, 0)
assert half_adder(0, 1) == (1, 0)
assert half_adder(1, 0) == (1, 0)
assert half_adder(1, 1) == (0, 1)
print("Verify Adder")
print("\t- Half Adder")

#                       sum <--.  .--> carry
#                              |  |

assert full_adder(0, 0, 0) == (0, 0)
assert full_adder(0, 0, 1) == (1, 0)
assert full_adder(0, 1, 0) == (1, 0)
assert full_adder(0, 1, 1) == (0, 1)
assert full_adder(1, 0, 0) == (1, 0)
assert full_adder(1, 0, 1) == (0, 1)
assert full_adder(1, 1, 0) == (0, 1)
assert full_adder(1, 1, 1) == (1, 1)
print("\t- Full Adder")

assert adder(byte(1), byte(128)) == byte(129)

# Testing 0's
assert adder(byte(0), byte(0)) == byte(0)

# Testing Cumulative Property. Simple math
assert adder(byte(7), byte(3)) == byte(10)
assert adder(byte(3), byte(7)) == byte(10)

# Testing Identity Property
assert adder(byte(0), byte(12)) == byte(12)
assert adder(byte(12), byte(0)) == byte(12)

# Testing boundaries
assert adder(byte(254), byte(1)) == byte(255)
assert adder(byte(128), byte(127)) == byte(255)

# Testing ripple carries
assert adder(byte(1), byte(1)) == byte(2)       # 1 carry.   No Overflow. 0000 0001 + 0000 0001 == 0000 0010
assert adder(byte(127), byte(1)) == byte(128)   # 7 carries. No Overflow. 0111 1111 + 0000 0001 == 1000 0000
assert adder(byte(255), byte(1)) == byte(0) == byte_tuple("0")       # 8 carries. Min Overflow. 1111 1111 + 0000 0001 == 0001 [0000 0000]
# assert adder(byte(255), byte(255)) == byte(254) == byte_tuple("11111110")   # 8 carries. Max Overflow. 1111 1111 + 1111 1111 == 0001 [1111 1110]

# Testing larger numbers; however, larger bytes are not allowed. My byte() function casts the number to 1 byte
assert byte(256) == byte(0)
assert byte(257) == byte(1)
assert adder(byte(256 + 0), byte(256 + 0)) == byte(0) == byte_tuple("0")
assert adder(byte(256 + 1), byte(256 + 2)) == byte(3) == byte_tuple("11")
assert adder(byte(256 + 16), byte(256 + 32)) == byte(48) == byte_tuple("00110000")
print("\t- 8-bit Adder")
