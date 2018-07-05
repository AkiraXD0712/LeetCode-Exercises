'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
'''


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def func(nums, res=None):
            if len(nums) == 1:
                return [nums]
            else:
                l1 = []
                buffer_list = []
                for i in range(len(nums)):
                    if nums[i] not in buffer_list:
                        buffer_list.append(nums[i])
                        for l in func(nums[:i]+nums[i+1:], [nums[i]]):
                            l1.append([nums[i]] + l)
            return l1
        return func(nums)