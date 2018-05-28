"""
Implement atoi to convert a string to an integer.

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits 
as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no 
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of 
representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        str = str.lstrip(' ')

        # if string don't start with digital number or plus/minus sign, return 0
        if not str[0].isdigit() and str[0] not in ['-', '+']:
            return 0

        # count number of not digital character
        i = 0
        while i < len(str) and not str[i].isdigit():
            i += 1
        # if string start with more than 1 plus/minus sign, return 0
        if i > 1:
            return 0
        else:
            # get all digital number before a not digital character
            j = 0
            while j < len(str[i:]) and str[i:][j].isdigit():
                j += 1
            # if string doesn't hava digital number, return 0
            if j == 0:
                return 0
            else:
                if int(str[0: i + j]) <= -2147483648:
                    return -2147483648
                elif int(str[0: i + j]) >= 2147483647:
                    return 2147483647
                else:
                    return int(str[0: i + j])


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
            str = stringToString(line);

            ret = Solution().myAtoi(str)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()