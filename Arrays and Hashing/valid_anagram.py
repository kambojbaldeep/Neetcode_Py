'''Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.'''

# Solution = https://www.youtube.com/watch?v=9UtInBqnCgA

# Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = []
        b = []

        for i in s:
            a.append(i)
        for j in t:
            b.append(j)

        a.sort()
        b.sort()

        if a==b:
            return True
        else:
            return False