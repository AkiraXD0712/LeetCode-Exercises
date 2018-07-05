'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def ascend(v1, v2):
            return True if v1 > v2 else False

        if len(nums) != 1:
            index1, value1 = None, None
            for i in range(1, len(nums)):
                if ascend(nums[i], nums[i - 1]):
                    index1, value1 = i - 1, nums[i - 1]

            if index1 is None:
                nums.reverse()
            else:
                index2, value2 = index1 + 1, nums[index1 + 1]
                for j in range(index1 + 1, len(nums)):
                    if nums[j] > value1 and nums[j] < value2:
                        index2, value2 = j, nums[j]
                nums[index1], nums[index2] = value2, value1

                l = sorted(nums[index1 + 1:])
                for k in range(index1 + 1, len(nums)):
                    nums[k] = l[k - index1 - 1]