"""
This module contains the implementation of the Longest Harmonious Subsequence problem.
The problem is to find the length of the longest harmonious subsequence in an array,
where a harmonious subsequence is defined as one where the maximum and minimum elements differ by exactly 1.
For example, in the array [1, 3, 2, 2, 5, 4, 3, 7], the longest harmonious subsequence is [3, 2, 2, 3] with length 4.
Funnily enough, I misread the problem and thought it was about finding the longest subnarray with a difference of 1,
within the array itself, so for the above example, I thought the answer was 3 ie [3, 2, 2]. In that implementation,
I used a sliding window approach, which was efficient for what I thought the problem was.
"""

from collections import Counter

class LHS:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        maxim = 0
        for key in count:
            if count[key-1] or count[key+1]:
                maxim = max(max(count[key-1], count[key+1])+count[key], maxim)
        return maxim