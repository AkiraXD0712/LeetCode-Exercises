import json
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Answer from: 
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def median(A, B):
            m, n = len(A), len(B)
            if m > n:
                A, B, m, n = B, A, n, m
            if n == 0:
                raise ValueError

            imin, imax, half_len = 0, m, (m + n + 1) // 2
            print(imin, imax)
            while imin <= imax:
                i = (imin + imax) // 2
                j = half_len - i
                if i < m and B[j - 1] > A[i]:
                    # i is too small, must increase it
                    imin = i + 1
                elif i > 0 and A[i - 1] > B[j]:
                    # i is too big, must decrease it
                    imax = i - 1
                else:
                    # i is perfect
                    if i == 0:
                        max_of_left = B[j - 1]
                    elif j == 0:
                        max_of_left = A[i - 1]
                    else:
                        max_of_left = max(A[i - 1], B[j - 1])

                    print(max_of_left)

                    if (m + n) % 2 == 1:
                        return max_of_left

                    if i == m:
                        min_of_right = B[j]
                    elif j == n:
                        min_of_right = A[i]
                    else:
                        min_of_right = min(A[i], B[j])

                    print(min_of_right)

                    return (max_of_left + min_of_right) / 2.0

        return median(nums1, nums2)


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
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);

            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()