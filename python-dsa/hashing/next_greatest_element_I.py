"""
While I brainstormed an O(n^2) solution, I learned that the O(n) solution can be implemented by using a stack on top of hashing.
This problem involves finding the next greater element for each element in nums1 from nums2.
For example, if nums1 = [4, 1, 2] and nums2 = [1, 3, 4, 2], the answer would be [-1, 3, -1].
This is because after 4 in nums2, there is no greater element, after 1 there is 3, and after 2 there is no greater element.
"""
class NextGreaterElementClass:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greater_element_map = {}
        for i in range(len(nums2)):
            if not stack or nums2[i] <= stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i] > stack[-1]:
                    greater_element_map[stack.pop()] = nums2[i]
                stack.append(nums2[i])
        for num in stack:
            greater_element_map[num] = -1
        return [greater_element_map.get(num, -1) for num in nums1]

