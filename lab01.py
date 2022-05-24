from typing import *
from helper_classes import *
import numpy as np
import os


def main():
    # experiment code

    map_s = {}
    map_s[1] = 1
    print(map_s[0])

    s = 'abb'
    t = 'acc'
    for i, (c1, c2) in enumerate(zip(s, t)):
        print(i, c1, c2)

    # done
    print('done')


if __name__ == '__main__':
    main()
