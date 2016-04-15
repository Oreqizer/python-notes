# Sorting:
# .sort() does an in-place sort if available
# sorted(obj) produces a new object

mutable = [5, 2, 4, 1, 3]
immutable = (5, 2, 4, 1, 3)

words = ("banana", "apple", "pineapple", "peach", "strawberry")


def newobj():
    newone = sorted(mutable)
    print(mutable)
    print(newone)


def inplace():
    mutable.sort()
    print(mutable)


def options():
    # reversed: simply does a reversed sort
    print(sorted(words, reverse=True))

    # key: function to used on the elements and sort them by the result
    # default is identity function (items themselves are compared)
    print(sorted(words, key=len))

    # we can combine the **kwargs
    print(sorted(words, reverse=True, key=len))


if __name__ == '__main__':
    print('> newobj')
    newobj()
    print('> inplace')
    inplace()
    print('> options')
    options()
