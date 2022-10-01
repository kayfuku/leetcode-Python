import random
from typing import *
from helper_classes import *
import numpy as np
import os
from collections import *


def main():
    # experiment code

    try:
        a = 1
        if a:
            raise Exception("!!")

    except Exception as e:
        print("exception catched. {}".format(e))

    # done
    print('done')


if __name__ == '__main__':
    main()
