# https://leetcode.com/problems/maximum-subarray/
# history: needed to see youtube video 
def max_sub_array(nums):
    current_sum = 0 
    max_sub = nums[0]

    for i in range(len(nums)):
        if nums[i]+current_sum < 0:
            max_sub = nums[i] if nums[i]> max_sub else max_sub
            current_sum = 0
            # print("for i:",i, " value:",nums[i]," current_sum",current_sum," max_sub",max_sub," skipping.....")
            continue
        
        current_sum += nums[i]
        max_sub = current_sum if current_sum > max_sub else max_sub
        # print("for i:",i, " value:",nums[i]," current_sum",current_sum," max_sub",max_sub)
    return max_sub
    


def max_sub_array_executor():
    print('max sub array')
    print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4])) # 6
    print(max_sub_array([1])) # 1
    print(max_sub_array([5,4,-1,7,8])) # 23
    
    