import random
from typing import *
from helper_classes import *
import numpy as np
import os
from collections import *
from sortedcontainers import SortedList


def main():
    # experiment code

    q = deque(['a', 'b', 'c'])
    for _ in range(len(q)):
        x = q.popleft()
        if x == 'b':
            a = 1
        else:
            q.append(x)
    print(q)

    # done
    print('done')


if __name__ == '__main__':
    main()
