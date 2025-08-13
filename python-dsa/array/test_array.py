import pytest

from max_subarray import SubArraySolution

@pytest.mark.parametrize(
    "nums, expected", 
    [
        ([1, -2, 3, 4, -1, 2, 1, -5, 4], 9),
        ([-2, -3, -1], -1),
        ([5, 4, -1, 7, 8], 23),
        ([1, 2, 3, 4, 5], 15),
        ([-1, -2, -3, -4], -1),
    ],
)
def test_max_subarray(nums, expected):
    solution = SubArraySolution()
    result = solution.maxSubArray(nums)
    assert result == expected, f"Expected {expected}, but got {result}"