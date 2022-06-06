from typing import *
from helper_classes import *
import numpy as np
import os


def main():
    # experiment code

    n = -23
    b = 26
    print(n // b)
    print(n - n // b * b)
    print(n % b)

    c = -4 % 3
    print(c)

    # done
    print('done')


if __name__ == '__main__':
    main()
