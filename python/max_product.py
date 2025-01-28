# https://leetcode.com/problems/maximum-product-subarray/
# historut 28/1/25 - 45 min
# Note: This solution won't come in mind during interview, need to memorize

# solution 1 
# def max_product(nums):
#     result = max(nums)
#     current_min,current_max = 1,1
     
#     for i in range(len(nums)):
#         if(nums[i]==0):
#             current_min =1 
#             current_max=1
#             result  = max(0,result)
#             continue
#         temp_min = current_min * nums[i]
#         temp_max = current_max * nums[i]
#         current_min = min(temp_min,temp_max,nums[i])
#         current_max = max(temp_min,temp_max,nums[i])
#         result = max(current_max ,result)
#     return result


    
# solution 2: same but more efficent
def max_product(nums):
    result = max(nums)
    current_min,current_max = 1,1
    
    for num in nums:
        if num==0:
            current_max,current_min = 1,1
            continue
        temp = current_max *num
        current_max = max( current_max* num, current_min* num,num)
        current_min = min (temp, current_min* num,num)
        result= max(current_max,result)
    
    return result
    


def max_product_executor():
    print('max profit')
    print(max_product([2,3,-2,4])) # 6
    print(max_product([-2,0,-1])) # 0
    print(max_product([3,-1,4])) #4
    