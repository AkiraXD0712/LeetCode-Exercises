'''
Given a collection of distinct integers, return all possible permutations.
'''


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def func(nums, res=None):
            if len(nums) == 1:
                return [nums]
            else:
                l1 = []
                for i in range(len(nums)):
                    for l in func(nums[:i]+nums[i+1:], [nums[i]]):
                        l1.append([nums[i]] + l)
            return l1
        return func(nums)