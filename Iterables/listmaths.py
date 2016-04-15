# * and + on lists:
# they always create a new item, don't mutate old ones
# they call __add__ and __mul__
#
# HOWEVER:
# += and *= call __iadd__ and __imul__, respectively.
# with the 'i' meaning in-place, but only if __iadd__ is defined,
# otherwise  __add__ is used, and the operation is not in-place


def multiply():
    # BEWARE: [[]] * 3 creates three references to the same list!
    # don't use with mutable values - they keep the same reference
    l = [1, 2, 3]
    print(l * 3)


# BEWARE: [[]] * 3 creates three references to the same list!
# don't use with mutable values - they keep the same reference
def tictactoe():
    # GOOD:
    board = [['_'] * 3 for _ in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)
    # BAD:
    weird = [['_'] * 3] * 3
    print(weird)
    weird[1][2] = 'X'
    print(weird)
    # it's like this:
    row = ['_'] * 3
    board = []
    for _ in range(3):
        board.append(row)  # same reference


# NEVER do this in real life.
# works, because the error occures after the +=
# so it is thrown, but the list is modified
def riddle():
    bollocks = (1, 2, [20, 30])
    print(bollocks)
    try:
        bollocks[2] += [40, 50]
    except TypeError:
        print("TypeError, cannot modify tuple. But it works.")
    finally:
        print(bollocks)


if __name__ == '__main__':
    print('> multiply')
    multiply()
    print('> tictactoe')
    tictactoe()
    print('> riddle')
    riddle()
