# https://leetcode.com/problems/product-of-array-except-self
# historut 27/1/25 - 30 min

# solution 1 with divide operator 
# def product_except_self(nums):
#     result =[]
#     max_product = 1
#     for each in nums:
#         if each !=0 :
#             max_product = max_product*each
#     if(nums.count(0)>1):
#         result = [0]*len(nums)
#     elif(nums.count(0)==1):
#         for each in nums:
#             if (each!=0):
#                 result.append(0)
#             else:
#                 result.append(max_product)
#     else:
#         result = [max_product//x for x in nums if x !=0 ]
#     return result
    

# solution 2 without divide operator
# def product_except_self(nums):
#     prefix=[nums[0]]
#     postfix=[nums[-1]]
#     result=[]
#     l=1
#     r=len(nums)-2
#     while (l<len(nums)):
#         prefix.append(prefix[l-1]*nums[l])
#         postfix.insert(0,postfix[0]*nums[r])
#         l+=1
#         r-=1
#     for index in range(len(nums)):
#         if (index==0):
#             result.append(postfix[index+1])
#         elif (index == len(nums)-1):
#             result.append(prefix[index-1])
#         else:
#             result.append(prefix[index-1]*postfix[index+1])
#     return result



# solution 3 without divide operator more efficient 
# def product_except_self(nums):
#     lenght = len(nums)
#     prefix =[None]*lenght
#     postfix = [None]*lenght
#     result=[None]*lenght

#     postfix[-1]=nums[-1]
#     for i in range(lenght-2,-1,-1):
#         postfix[i] = postfix[i+1] * nums[i]

#     prefix[0]=nums[0]
#     result[0] = postfix[1]
#     for i in range(1,lenght,+1):
#         prefix[i] = prefix[i-1]*nums[i]
#         if( i == lenght-1):
#             result[i]= prefix[i-1]
#         else:
#             result[i] = prefix[i-1]*postfix[i+1]

#     return result

# solution 4 without divide operator most efficient but difficult to remember
def product_except_self(nums):
    length = len(nums)
    result=[1]*length

    prefix =1 
    for i in range(length):
        result[i]= prefix
        prefix = prefix* nums[i]

    postfix =1 
    for i in range(length-1,-1,-1):
        result[i] = result[i]*postfix
        postfix = postfix * nums[i]

    return result


def product_except_self_executor():
    print('product except self')
    print(product_except_self([1,2,3,4])) # [24,12,8,6]
    print(product_except_self([-1,1,0,-3,3])) # [0,0,9,0,0]
    print(product_except_self([0,0])) # [0,0]
