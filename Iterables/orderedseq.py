# Managing ordered sequences:
# bisect module:
# - bisect
# - insort
# used for inserting and searching values
# while keeping a sequence ordered
# see: Raymond Hettinger: SortedCollection

import bisect
import random

SIZE = 7

random.seed(1729)

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FORMAT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


# INSORT:
def inserting():
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)


# BISECT:
def printer(fn):
    for needle in reversed(NEEDLES):
        position = fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FORMAT.format(needle, position, offset))


# if ==, needle on the right
def regular():
    # bisect.bisect(haystack, needle)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    printer(bisect.bisect)


# if ==, needle on the left
def left():
    # bisect.bisect_left(haystack, needle)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    printer(bisect.bisect_left)


if __name__ == '__main__':
    print('> inserting()')
    inserting()
    print('> regular')
    regular()
    print('> left')
    left()