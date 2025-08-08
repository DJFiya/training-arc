"""
Working through LeetCode 599: Minimum Index Sum of Two Lists.

I struggled with my initial approach using heapq which only tracked the minimum index sum but
failed to collect all restaurants with the same minimum index sum. I considered using a defaultdict
to group by index sum, but that felt clunky and inefficient. Overall my initial solutions were memory intensive
and not very optimal.

The clean solution below uses a single pass and a map for efficient lookup, collecting all results with the minimum index sum.
"""


class MinimumIndexSumOfTwoLists():
    def findRestaurant(self, list1, list2):
        index_map = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, s in enumerate(list2):
            if s in index_map:
                total_index = j + index_map[s]
                if total_index < min_sum:
                    min_sum = total_index
                    result = [s]
                elif total_index == min_sum:
                    result.append(s)
        return result
