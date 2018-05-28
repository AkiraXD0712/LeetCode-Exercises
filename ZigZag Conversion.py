class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        buff_dict = {}
        for k, v in enumerate(s):
            n = abs((k % (2 * numRows - 2) + 1) - numRows) + 1
            n = abs(numRows - n)
            if n not in buff_dict:
                buff_dict[n] = v
            else:
                buff_dict[n] += v
        return ''.join(buff_dict.values())


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
            line = next(lines)
            numRows = int(line);

            ret = Solution().convert(s, numRows)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()