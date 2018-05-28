import json
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Manacher Algorithem:
https://segmentfault.com/a/1190000003914228
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        p = [1] * len(s)
        pos, maxRight = 0, 0
        center, maxLen = 0, 0
        for i in range(len(s)):
            j = pos - (i - pos)
            p[i] = min(p[j], maxRight - i) if maxRight >= i else 1
            while i - p[i] >= 0 and i + p[i] < len(s) and s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            if i + p[i] - 1 > maxRight:
                maxRight = i + p[i] - 1
                pos = i
            if p[i] > maxLen:
                maxLen = p[i]
                center = i

        return s[center - (maxLen - 1): center + (maxLen - 1)].replace("#", "")


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().longestPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()