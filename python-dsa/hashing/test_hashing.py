"""Testing file for all hashing problems."""
import pytest

from next_greatest_element_I import NextGreaterElementClass

@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1, 2, 3], [3, 2, 1], [-1, -1, -1]),
        ([5], [5], [-1]),
        ([10, 20], [20, 10], [-1, -1]),
    ]
)
@pytest.mark.asyncio
async def test_next_greater_element(nums1, nums2, expected):
    solution = NextGreaterElementClass()
    result = solution.nextGreaterElement(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"