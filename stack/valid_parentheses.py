# Author: leetcode + kei
# Date: July 17, 2021
from typing import *
from helper_classes import *


class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        if len(s) == 1:
            return False

        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if not c in mapping:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if mapping[c] != top:
                    return False

        return len(stack) == 0


class Solution2:
    """ leetcode solution """

    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))
    string = ''
    print(s.isValid(string))


if __name__ == '__main__':
    main()
