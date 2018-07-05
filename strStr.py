'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
'''


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        start = needle[0]
        for i in range(len(haystack)):
            if start == haystack[i]:
                if i+len(needle) <= len(haystack):
                    if haystack[i: i+len(needle)] == needle:
                        return i
                else:
                    return -1
        return -1