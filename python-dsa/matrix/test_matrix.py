"""Testing file for all matrix problems."""
import pytest

from flood_fill import FloodFill

@pytest.mark.parametrize(
    "image, sr, sc, color, expected",
    [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 1, 1]], 0, 0, 2, [[2, 2, 2], [2, 1, 1]]),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1, 1, 2, [[1, 1, 1], [1, 2, 1], [1, 1, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 1, [[1, 1, 1], [1, 1, 1]]),
        ([[1]], 0, 0, 2, [[2]]),
    ]
)
@pytest.mark.asyncio
async def test_flood_fill(image, sr, sc, color, expected):
    solution = FloodFill()
    result = solution.floodFill(image, sr, sc, color)
    assert result == expected, f"Expected {expected}, but got {result}"

