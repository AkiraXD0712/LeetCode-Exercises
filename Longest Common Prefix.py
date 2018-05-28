"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for k, v in enumerate(strs):
            if k == 0:
                prefix = v
            else:
                i = 0
                while i <= min(len(v), len(prefix)) and v[:i] == prefix[:i]:
                    i += 1
                prefix = prefix[:i-1]
        return prefix