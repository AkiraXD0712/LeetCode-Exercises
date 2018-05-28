"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(-x)[::-1])

        return x if (x <= 2 ** 31 - 1) and (x >= -2 ** 31) else 0


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = int(line);

            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()