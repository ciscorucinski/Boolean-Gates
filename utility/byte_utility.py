from utility.alias import Byte, Nibble


def byte(number: int) -> Byte:
    return Byte(
        bit8=(number & 128) // 128,
        bit7=(number & 64) // 64,
        bit6=(number & 32) // 32,
        bit5=(number & 16) // 16,
        bit4=(number & 8) // 8,
        bit3=(number & 4) // 4,
        bit2=(number & 2) // 2,
        bit1=(number & 1) // 1
    )


def nibble(number: int) -> Nibble:
    return Nibble(
        (number & 8) // 8,
        (number & 4) // 4,
        (number & 2) // 2,
        (number & 1) // 1
    )


def byte_tuple(byte: str) -> Byte:

    bytes = {
        f"bit{i + 1}": int(number)
        for i, number
        in enumerate(reversed(byte.rjust(8, "0")))
        if i < 8
    }

    return Byte(**bytes)


def negate_byte(byte: Byte) -> Byte:
    bytes = {
        f"bit{i + 1}": 0 if bit else 1
        for i, bit
        in enumerate(byte)
    }

    return Byte(**bytes)
