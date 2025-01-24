# problem: https://leetcode.com/problems/two-sum/description/
# historut 25/1/25 - 25 min

# solution 1
def two_sum(nums, target):
    my_dict={}
    for index in range(len(nums)):
        difference = target-nums[index]
        if (difference in my_dict):
            return [my_dict[difference][1],index]
        else:
            my_dict[nums[index]]=[difference,index]

