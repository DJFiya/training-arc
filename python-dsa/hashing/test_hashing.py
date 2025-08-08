"""Testing file for all hashing problems."""
import pytest

from next_greatest_element_I import NextGreaterElementClass
from keyboard_row import KeyboardRow
from distribute_candies import CandyDistribution
from longest_harmonius_subsequence import LHS
from minimum_index_sum_of_two_lists import MinimumIndexSumOfTwoLists

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

@pytest.mark.parametrize(
    "words, expected",
    [
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
        (["omg", "hello", "world"], []),
        (["qwerty", "asdfghjkl", "zxcvbnm"], ["qwerty", "asdfghjkl", "zxcvbnm"]),
        (["abc", "defg", "hij"], []),
        ([], []),
    ]
)
@pytest.mark.asyncio
async def test_keyboard_row(words, expected):
    solution = KeyboardRow()
    result = solution.findWords(words)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize(
    "candyType, expected",
    [
        ([1, 1, 2, 2, 3, 3], 3),
        ([1, 1, 2, 3], 2),
        ([1, 1, 1, 1], 1),
        ([1, 2, 3, 4, 5, 6], 3),
        ([1, 2], 1),
    ]
)
@pytest.mark.asyncio
async def test_distribute_candies(candyType, expected):
    solution = CandyDistribution()
    result = solution.distributeCandies(candyType)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 2, 2, 5, 4, 3, 7], 4),
        ([1, 2, 3, 4], 2),
        ([1, 1, 1, 1], 0),
        ([1, 2, 2, 3], 3),
        ([5, 5, 5, 5], 0),
    ]
)
@pytest.mark.asyncio
async def test_longest_harmonious_subsequence(nums, expected):
    solution = LHS()
    result = solution.findLHS(nums)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
         ["Shogun"]),
        (["Shogun", "KFC"], ["KFC", "Shogun"], ["KFC", "Shogun"]),
        (["A", "B", "C"], ["D", "E", "F"], []),
        (["A", "B", "C"], ["B", "A", "C"], ["A", "B"]),
        (["A"], ["A"], ["A"]),
    ]
)
@pytest.mark.asyncio
async def test_minimum_index_sum_of_two_lists(list1, list2, expected):
    solution = MinimumIndexSumOfTwoLists()
    result = solution.findRestaurant(list1, list2)
    assert set(result) == set(expected), f"Expected {expected}, but got {result}"