import random
from typing import *
from helper_classes import *
import numpy as np
import os
from collections import *
from sortedcontainers import SortedList


def main():
    # experiment code

    a = [(3, 0), (1, 3), (5, 2), (4, 1)]
    sorted_list = SortedList(a, key=lambda x: x[0])
    print(sorted_list)

    # done
    print('done')


if __name__ == '__main__':
    main()
