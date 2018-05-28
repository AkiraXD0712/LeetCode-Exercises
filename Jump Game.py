import json
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        graph = {}
        for i in range(len(nums) - 1):
            graph[i] = {i + j: j for j in range(1, nums[i] + 1)}

        graph[len(nums) - 1] = {-1: -1}

        def find_path(graph, start, end, path=None):
            if not path:
                path = []
            path = path + [start]
            if start == end:
                return path
            if start not in graph:
                return None
            for node in graph[start]:
                if node not in path:
                    newpath = find_path(graph, node, end, path)
                    if newpath: return newpath
            return None

        return True if find_path(graph, 0, len(nums) - 1) else False


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().canJump(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()