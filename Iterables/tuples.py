# Tuples as Lists:
# immutable, of course
# they share all the read-stuff, but lack the mutability
# EXCEPTION: reverse(tuple)

letters = ('a', 'b', 'c', 'd', 'e', 'f')


def slicing():
    # slicing is [startindex:endindex + 1] - why?
    first_half = letters[:3]
    second_half = letters[3:]

    # readability
    # this cuts the list/tuple to half
    # introduced by Dijkstra
    print(first_half)
    print (second_half)


def steps():
    third = letters[::3]  # takes every third
    reverse = letters[::-1]  # reverses
    reversed_second = letters[::-2]  # takes every second, starting at -1

    # [1:2:3] is the same as slice(start, stop, step)
    # works like this: letters.__getitem__(slice(start, stop, step))
    print(third)
    print(reverse)
    print(reversed_second)


def sliceobject():
    # YYYY-MM-DD
    year = slice(0, 4)
    month = slice(5, 7)
    day = slice(8, 10)
    someday = '1993-28-10'
    # we can use slice objects to get parts
    print('{}. {}. {}'.format(someday[day], someday[month], someday[year]))


def inplace():
    # NOTE: when left side is a slice,
    # right side must be an iterable
    l = list(range(10))  # [0, 1, 2, 3, 4...]
    print(l)
    l[2:5] = [20, 30]  # [0, 1, 20, 30, 5...]
    print(l)
    del l[5:7]  # removes 6, 7
    print(l)
    l[3::2] = [11, 22]  # replace index 3 with 11, then two after that with 22
    print(l)
    l[2:5] = [100]  # replaces index 2 to 4 with a single 100
    print(l)


# Ellipsis (...):
# alias of the Ellpsis object, single instance of the ellipsis class
# used mainly in NumPy
# useful for, let's say, multi-dimensional slices
# [1:5, :, :, :] is [1:5, ...]


if __name__ == '__main__':
    print('> slicing')
    slicing()
    print('> steps')
    steps()
    print('> sliceobject')
    sliceobject()
    print('> inplace')
    inplace()

