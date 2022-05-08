from typing import *
from helper_classes import *
import numpy as np
import os


def main():
    # experiment code

    c = []
    d = []

    def ap(_d=None):
        d.append('a')
        d.append('b')
        _d.append('c')

    ap(c)
    print('c:', c)

    ap(c)
    la = d.copy()
    print('la:', la)
    d.clear()
    print('d:', d)
    ap(c)
    lb = d.copy()
    print('lb:', lb)

    print(''.join(lb))

    # done
    print('done')


if __name__ == '__main__':
    main()
