"""Tests for binary search problems."""

import pytest

from first_bad_version import firstBad
@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 4),
        (1, 1),
        (10, 4),
        (7, 4),
        (2, 2),
    ]
)
@pytest.mark.asyncio
async def test_first_bad_version(n, expected):
    solution = firstBad(bad_version=expected)
    result = await solution.firstBadVersion(n)
    assert result == expected, f"Expected {expected}, but got {result}"