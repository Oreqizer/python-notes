# Listcomps (list comprehensions):
# used for producing new lists
# not good for stuff like cartesian product and such
# as they are kept in memory as a whole

symbols = '@#$%^&'


def potato():
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))

    print('Potato: {}'.format(codes))


def listcomp():
    codes = [ord(symbol) for symbol in symbols]
    print('Listcomp: {}'.format(codes))


def cartesian():
    ranks = ['A', 'Q', 'K']
    suits = ['spades', 'diamonds', 'clubs', 'hearts']
    cards = [(rank, suit) for suit in suits for rank in ranks]
    print('Cartesian product: {}'.format(cards))


# Python 2:
# variables were getting overwritten in listcomp
def variable():
    x = 'Outside'
    print('x before listcomp: {}'.format(x))
    codes = [ord(x) for x in 'ABC']
    print('x after listcomp: {}'.format(x))
    print('Listcomp in "variables": {}'.format(codes))


if __name__ == '__main__':
    print('> potato')
    potato()
    print('> listcomp')
    listcomp()
    print('> cartesian')
    cartesian()
    print('> variable')
    variable()
