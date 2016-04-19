# Queues:
# efficient .append, .pop, shifting etc.

from collections import deque


def dequing():
    dq = deque(range(10), maxlen=10)
    print(dq)
    # we can rotate queue
    dq.rotate(3)
    print(dq)
    # ...also negatively
    dq.rotate(-3)
    print(dq)
    # appending values throws excess ones away
    # from the opposite side
    # .append takes values
    dq.append(10)
    print(dq)
    # extend is the same, but takes iterables
    dq.extend([20])
    print(dq)
    # they have a 'left' equivalent
    dq.appendleft(-10)
    dq.extendleft([-20, -30])
    print(dq)


# queues implemented in:
# - queue
# - multiprocessing
# - asyncio
# - heapq


if __name__ == '__main__':
    print('> dequing')
    dequing()