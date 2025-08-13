"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum. My original solution, since I was coding from
scratch, was a bit more verbose version of Kadane's algorithm, but I later simplified it
to a more concise implementation that captures the essence of the algorithm, based on
reviewing the problem and understanding the optimal approach. However, I still find the
initial verbose version useful for understanding the step-by-step logic, and I am happy
that I was able to solve it with a decent solution without needing to do preliminary
research or look up the problem.
"""

class SubArraySolution():
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        running_sum = max_sum
        for i in range(1, len(nums)):
            running_sum = max(nums[i], running_sum + nums[i])
            max_sum = max(max_sum, running_sum)
            
        return max_sum
