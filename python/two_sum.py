# problem: https://leetcode.com/problems/two-sum/description/
# history 25/1/25 - 25 min

# solution 1
def two_sum(nums, target):
    my_dict={}
    for index in range(len(nums)):
        difference = target-nums[index]
        if (difference in my_dict):
            return [my_dict[difference][1],index]
        else:
            my_dict[nums[index]]=[difference,index]


def two_sum_executor():
    print("two sum")
    print(two_sum([2,7,11,15],9)) # [0,1]
    print(two_sum([3,2,4],6)) # [1,2]
    print(two_sum([3,3],6)) # [0,1]