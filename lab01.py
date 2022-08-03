from re import A
from typing import *
from helper_classes import *
import numpy as np
import os
from collections import deque


def main():
    # experiment code
    a = [1, 2]
    b = []
    b.append(a)
    print(b)
    a += [3]
    print(b)
    b.append(a)
    print(b)
    a.pop()
    print(b)
    b.append(a[:])  # Create a new list containing elements in list a.
    print(b)
    a += [3]
    print(b)

    # done
    print('done')


if __name__ == '__main__':
    main()
