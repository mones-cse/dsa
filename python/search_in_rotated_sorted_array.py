# https://leetcode.com/problems/search-in-rotated-sorted-array/
# history : 2h

# psudo code 

# # solution 1 
# # find midle in left section or right section 
# # if middle > left -> its left section 
# # if target < left -> check MR 
# # if target > left -> check either MR | LM 
# #   if target <= middel -> check LM
# #   else (target > middel) -> check RM 

# # if middle < left -> its right section 
# # if target < middle -> check LM 
# # if target > middle-> check either MR | LM
# #   if target >= right -> LM
# #   else (target < right) -> RM 
# def search_in_rotated_sorted_array(nums,target):
#     length = len(nums)
#     left = 0 
#     right = length-1
#     middle = length//2
#     if(length==1):
#         return 0 if nums[0]==target else -1
#     if (length==2):
#         if(nums[0]==target):
#             return 0
#         elif(nums[1]==target):
#             return 1
#         else:
#             return -1


#     while(left!=middle and right!=middle):
#         # print("🚀 ~ left:", nums[left],nums[middle],nums[right],left!=middle ,right!=middle)

        
#         if(nums[left]==target):
#             return left
#         elif(nums[middle]==target):
#             return middle
#         elif(nums[right]==target):
#             return right
        
#         if(nums[middle] > nums[left]):
#             # left section
#             if (target<nums[left]):
#                 # MR
#                 left=middle
#                 middle = middle+(right-middle)//2
#             else:
#                 if (target<= nums[middle]):
#                     # LM
#                     right = middle
#                     middle = left + (middle-left)//2
#                 else:
#                     # MR
#                     left=middle
#                     middle = middle+(right-middle)//2
#         else:
#             # right section
#             if (target < nums[middle]):
#                 # LM
#                 right = middle
#                 middle = left + (middle-left)//2
#             else:
#                 if(target >= nums[right]):
#                     #MR
#                     right = middle
#                     middle = left + (middle-left)//2
#                 else:
#                     #LM
#                     left=middle
#                     middle = middle+(right-middle)//2

#     return -1



# ----------------------------------------------------



# solution 2: minified
# find midle in left section or right section 
# if middle > left -> its left section 
#   if(target  > left and target <= middel) -> LM
#   else -> MR
# else ->its right section 
#   if (target > middle and target < right ) -> RM 
#   else LM 

# def search_in_rotated_sorted_array(nums,target):
#     length = len(nums)
#     left = 0 
#     right = length-1
#     middle = length//2
#     if(length==1):
#         return 0 if nums[0]==target else -1
#     if (length==2):
#         if(nums[0]==target):
#             return 0
#         elif(nums[1]==target):
#             return 1
#         else:
#             return -1


#     while(left!=middle and right!=middle):
        
#         if(nums[left]==target):
#             return left
#         elif(nums[middle]==target):
#             return middle
#         elif(nums[right]==target):
#             return right
        
#         if(nums[middle] > nums[left]):
#             # left section
#             if ( nums[middle] >= target >nums[left] ):#LM
#                 right =middle
#                 middle = left +(middle-left)//2
#             else:#MR
#                 left=middle
#                 middle = middle + (right-middle)//2
#         # right section
#         else:
#             if( nums[right] > target > nums[middle]):#LM
#                 left=middle
#                 middle = middle + (right-middle)//2
#             else:#MR
#                 right =middle
#                 middle = left +(middle-left)//2
#     return -1


# solution 3
def search_in_rotated_sorted_array(nums, target):
    if not nums:
        return -1
    left , right = 0 , len(nums)-1

    while left <=right:
        middle = (left+right)//2

        if nums[middle]==target:
            return middle
        
        # check if left half is sorted 
        if (nums[middle]>=nums[left]):
            if( nums[left]<=target <=nums[middle]):
                right=middle-1
            else:
                left = middle+1
        # right half is sorted
        else:
            if(nums[middle]<=target<=nums[right]):
                left = middle+1
            else:
                right = middle-1

    return -1














def search_in_rotated_sorted_array_executor():
    print(search_in_rotated_sorted_array([],1),-1) #-1
    print(search_in_rotated_sorted_array([8,9,2,3,4],9),1) #1
    print(search_in_rotated_sorted_array([1,3],1),0) #0
    print(search_in_rotated_sorted_array([3,1],1),1) #0
    print(search_in_rotated_sorted_array([7,8,1,2,3,4,5,6],2),3) #3
    print(search_in_rotated_sorted_array([1],1),0) #0
    print(search_in_rotated_sorted_array([1],0),-1) #-1
    print(search_in_rotated_sorted_array([4,5,6,7,0,1,2],0),4) #4
    print(search_in_rotated_sorted_array([4,5,6,7,0,1,2],3),-1) #-1

