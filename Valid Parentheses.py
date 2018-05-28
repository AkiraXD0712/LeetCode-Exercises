"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        buff_dict = {'{': 1, '}': -1, '(': 2, ')': -2, '[': 3, ']': -3}
        res = []
        for i in range(len(s)):
            if buff_dict[s[i]] > 0:
                res.append(buff_dict[s[i]])
            else:
                if not res:
                    return False

                if buff_dict[s[i]] + res[-1] != 0:
                    return False
                else:
                    res.pop()

        return True if not res else False