"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        check_list1 = []
        for k, v in enumerate(nums):

            if v in check_list1:
                continue

            length = len(result)
            l = nums[k + 1:]

            for k1, v1 in enumerate(l):

                l1 = l[k1 + 1:]

                if -(v + v1) in set(l1) and sorted([v, v1, -(v + v1)]) not in result:
                    result.append(sorted([v, v1, -(v + v1)]))
                else:
                    pass

            if length == len(result):
                check_list1.append(v)

        return result


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# 136ms
class Solution:
    def threeSum(self, nums):
        freq = {}
        for elem in nums:
            freq[elem] = freq.get(elem, 0) + 1
        if 0 in freq and freq[0] > 2:
            res = [[0,0,0]]
        else:
            res = []
        neg = sorted((filter(lambda x: x < 0, freq)))
        nneg = sorted((filter(lambda x: x>= 0, freq)))
        for elem1 in neg:
            for elem2 in nneg:
                src = -(elem1 + elem2)
                if src in freq:
                    if src in (elem1, elem2) and freq[src] > 1:
                        res.append([elem1, src, elem2])
                    elif src < elem1:
                        res.append([elem1, src, elem2])
                    elif src > elem2:
                        res.append([elem1, src, elem2])
        return res