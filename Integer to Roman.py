"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        if num // 1000 > 0:
            for i in range(num // 1000):
                s += 'M'
            s += self.intToRoman(num % 1000)
        elif num // 100 > 0:
            if 1 <= num // 100 <= 3:
                for i in range(num // 100):
                    s += 'C'
                s += self.intToRoman(num % 100)
            elif num // 100 == 4:
                s += 'CD' + self.intToRoman(num % 100)
            elif num // 100 == 5:
                s += 'D' + self.intToRoman(num % 100)
            elif 6 <= num // 100 <= 8:
                s += 'D'
                for i in range(num // 100 - 5):
                    s += 'C'
                s += self.intToRoman(num % 100)
            elif num // 100 == 9:
                s += 'CM' + self.intToRoman(num % 100)
        elif num // 10 > 0:
            if 1 <= num // 10 <= 3:
                for i in range(num // 10):
                    s += 'X'
                s += self.intToRoman(num % 10)
            elif num // 10 == 4:
                s += 'XL' + self.intToRoman(num % 10)
            elif num // 10 == 5:
                s += 'L' + self.intToRoman(num % 10)
            elif 6 <= num // 10 <= 8:
                s += 'L'
                for i in range(num // 10 - 5):
                    s += 'X'
                s += self.intToRoman(num % 10)
            elif num // 10 == 9:
                s += 'XC' + self.intToRoman(num % 10)
        elif num // 1 > 0:
            if 1 <= num // 1 <= 3:
                for i in range(num // 1):
                    s += 'I'
            elif num // 1 == 4:
                s += 'IV'
            elif num // 1 == 5:
                s += 'V'
            elif 6 <= num // 1 <= 8:
                s += 'V'
                for i in range(num // 1 - 5):
                    s += 'I'
            elif num // 1 == 9:
                s += 'IX'
            return s
        return s


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            num = int(line);

            ret = Solution().intToRoman(num)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()