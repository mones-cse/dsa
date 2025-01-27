# problem: https://leetcode.com/problems/contains-duplicate/
# historut 25/1/25 - 10 min

# solution 1
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
def contains_duplicate(nums):
    return len(nums)!=len(set(nums))

def contains_duplicate_executor():
    print('contains duplicate')
    contains_duplicate([1,2,3,1]) # true
    contains_duplicate([1,2,3,4]) # false
    contains_duplicate([1,2,3,1]) # true