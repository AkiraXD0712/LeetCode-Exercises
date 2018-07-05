'''
Given an unsorted integer array, find the smallest missing positive integer.

Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = 1
        for item in sorted(nums):
            if item == smallest:
                smallest += 1
        return smallest