from multiprocessing.connection import wait
from typing import *
from helper_classes import *
import numpy as np
import os


def main():
    # experiment code
    wait_count = {}

    wait_count[3] = 1
    print(wait_count)

    for k, v in wait_count.items():
        wait_count[k] -= 1
    print(wait_count)

    print(wait_count[k] == 0)

    # done
    print('done')


if __name__ == '__main__':
    main()
