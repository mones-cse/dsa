# create a basic python code that will run contains_duplicate function
# and print the result

from contains_duplicate import contains_duplicate
from two_sum import two_sum

def main():
#    https://leetcode.com/problems/contains-duplicate/description/
#    contains_duplicate([1,2,3,1]) # true
#    contains_duplicate([1,2,3,4]) # false
#    contains_duplicate([1,2,3,1]) # true
#    -------------------------------------------------------------
#    https://leetcode.com/problems/two-sum/description/
    print(two_sum([2,7,11,15],9)) # [0,1]
    print(two_sum([3,2,4],6)) # [1,2]
    print(two_sum([3,3],6)) # [0,1]


if __name__ == "__main__":
   main()
