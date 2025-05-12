''' Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false  '''

# Video Explanation : https://www.youtube.com/watch?v=3OamzN90kPg

# Solution:

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = []
        for i in nums:
            if i not in d:
                d.append(i)

        if nums==d:
            return False
        else:
            return True