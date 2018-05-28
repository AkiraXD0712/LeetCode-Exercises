import json
"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def get_axe_length(nums, k):

            l = len(nums)
            r = l // 2 - 1 if l % 2 == 0 else l // 2

            l1 = len(nums[:l - k])
            r1 = l1 // 2 - 1 if l1 % 2 == 0 else l1 // 2

            l2 = k
            r2 = l2 // 2 - 1 + l1 if l2 % 2 == 0 else l2 // 2 + l1

            return [(l1, r1), (l2, r2), (l, r)]

        if len(nums) != 1:
            if k > len(nums):
                k -= len(nums)
            list_axe_length = get_axe_length(nums, k)

            for item in list_axe_length:
                if item[0] % 2 == 0:
                    for i in range(item[0] // 2):
                        val = nums[item[1] - i]
                        nums[item[1] - i] = nums[item[1] + 1 + i]
                        nums[item[1] + i + 1] = val
                else:
                    for i in range(item[0] // 2):
                        val = nums[item[1] - 1 - i]
                        nums[item[1] - 1 - i] = nums[item[1] + 1 + i]
                        nums[item[1] + 1 + i] = val


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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
            line = next(lines)
            k = int(line);

            ret = Solution().rotate(nums, k)

            out = integerListToString(nums)
            if ret is not None:
                print("Do not return anything, modify nums in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()