"""
This module contains the implementation of distribute candies problem.
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight,
so she visited a doctor. The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while
still following the doctor's advice.
This is a simple problem but still is hashing.
"""

class CandyDistribution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(candyType)//2, len(set(candyType)))
        