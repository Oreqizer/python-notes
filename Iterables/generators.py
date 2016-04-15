# Genexps (generator expressions):
# generated lazily - not kept in memory
# as opposed to listcomps (they generate list and feed the constructor)

import array

symbols = '@#$%^&'


def tuples():
    print(tuple(ord(symbol) for symbol in symbols))


def arrays():
    print(array.array('I', (ord(symbol) for symbol in symbols)))


def cartesian():
    colors = ['black', 'red']
    sizes = ['S', 'M', 'L']
    for shirt in ('%s %s' % (size, color) for color in colors for size in sizes):
        print(shirt)


if __name__ == '__main__':
    print('> tuples')
    tuples()
    print('> arrays')
    arrays()
    print('> cartesian')
    cartesian()
