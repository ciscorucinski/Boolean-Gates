def bits_8(num):
    return ((num & 128) // 128,
            (num & 64) // 64,
            (num & 32) // 32,
            (num & 16) // 16,
            (num & 8) // 8,
            (num & 4) // 4,
            (num & 2) // 2,
            (num & 1) // 1)


def bits_4(num):
    return ((num & 8) // 8,
            (num & 4) // 4,
            (num & 2) // 2,
            (num & 1) // 1)
