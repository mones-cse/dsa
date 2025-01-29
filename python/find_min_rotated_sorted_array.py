# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# history : 2h
def find_min_rotated_sorted_array(nums):
    length = len(nums)
    if (length==1):
            return nums[0]
    left = 0
    right = length-1
    middle = length//2
    while (left!= middle and middle!=right):
        if (nums[middle] < nums[right]):
            right = middle
            middle = left + (middle-left)//2
        else:
            left = middle
            middle = middle + (right-middle)//2
            
    return min(nums[left],nums[right])


def find_min_rotated_sorted_array_executor():
    print(find_min_rotated_sorted_array([2,1])) #1
    print(find_min_rotated_sorted_array([1,99])) #1
    print(find_min_rotated_sorted_array([1,2,3,4,5,6,7,88,9])) #1
    print(find_min_rotated_sorted_array([7,8,9,1,2,3,4,5,6])) #1
    print(find_min_rotated_sorted_array([3,4,5,6,7,8,99,1,2])) #1
    print(find_min_rotated_sorted_array([2,3,4,5,6,7,8,9])) #2
    print(find_min_rotated_sorted_array([9,1,2,3,4,5,6,7,8])) #1
