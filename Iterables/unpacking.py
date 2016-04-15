# Unpacking:
# just what you'd expect.
# use * to capture a group, not only at the end, but anywhere

import os


def swap():
    x, y = 5, 7
    print(x, y)
    y, x = x, y
    print(x, y)


def capture():
    print(divmod(20, 8))
    t = (20, 8)
    print(divmod(*t))
    quotient, remainder = divmod(*t)
    print(quotient, remainder)


def filenaming():
    _, filename = os.path.split('/home/oreqizer/.ssh/idrsa.pub')
    print(filename)


def excess():
    x, y, *rest = range(5)
    print(x, y, rest)
    x, *body, y = range(5)
    print(x, body, y)
    *head, x, y = range(5)
    print(head, x, y)


# if we match the nesting structure, we can do nested unpacking
def nested():
    vectors = [
        ('vector1', (5, 7, 2)),
        ('vector2', (3, 1, 9)),
        ('vector3', (4, 5, 3))
    ]
    for name, (x, y, z) in vectors:
        print('{}: x = {}, y = {}, z = {}'.format(name, x, y, z))


# Python 3:
# cannot define a function like so:
# def fn(x, (a, b), y):
# see PEP 3113 - Removeal of Tuple Parameter Unpacking


if __name__ == '__main__':
    print('> swap')
    swap()
    print('> capture')
    capture()
    print('> filenaming')
    filenaming()
    print('> excess')
    excess()
    print('> nested')
    nested()
