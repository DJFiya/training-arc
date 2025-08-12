"""
A little more challenging than simple binary search, this problem requires
a bit of thought to implement correctly, since you need to minimize the number
of API calls to check if a version is bad.
"""

import asyncio

class firstBad():
    def __init__(self, bad_version):
        self.bad_version = bad_version

    async def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, mid, high = 1, (n+1)//2, n
        while low <= high:
            state = await self.isBadVersion(mid)
            if state:
                high, mid = mid, (mid+low)//2
            else:
                low, mid = mid, (mid+high)//2
            if high-low <= 1:
                return low if await self.isBadVersion(low) else high
    
    async def isBadVersion(self, version):
        """
        Mock function to simulate the API call.
        In a real scenario, this would check if the version is bad.
        """
        await asyncio.sleep(0.1)
        return version >= self.bad_version