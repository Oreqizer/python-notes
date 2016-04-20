# Arrays:
# a lot more compact than lists
# because only stores primitives, not objects.
# supports all mutable sequence operations, and more
# for fast loading/saving

from array import array
from random import random
import os


def speed():
    # double is 8 bytes
    # we're going to store 80 000 000 bytes to a file
    # that's 80MB of numbers. that's a LOT
    floats = array('d', (random() for _ in range(10**7)))  # 10 000 000 doubles
    fp = open('floats.bin', 'wb')
    # write to file
    floats.tofile(fp)
    fp.close()
    # copy from file
    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()
    print('Floats equal: {}'.format(floats[-1] == floats2[-1]))
    os.remove('floats.bin')


# Memoryview:
# allows handling slices of arrays without copying
def memview():
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    # now they share memory access
    print(len(memv))
    print(memv[0])
    # .cast() returns a new memoryview
    # changing the way the bytes are handled
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    # oct: 04 00 -> bin: 0000 0100 0000 0000 -> dec: 2 ^ 10 -> 1024
    print(numbers)


# NumPy and SciPy:
# not included, as they are not part of the standard library
# they include a vast number of operations with multidimensional
# arrays, data, statistics, matrices, advanced arrays etc...


if __name__ == '__main__':
    print('> speed')
    speed()
    print('> memview')
    memview()
