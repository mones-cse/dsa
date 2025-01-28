# problem: https://leetcode.com/problems/container-with-most-water/
# history 28/1/25 - 25 min

# solution 1
def water_area(height):
    l=0
    r= len(height)-1
    max_contain =0

    while (l!=r):
        temp = min(height[l],height[r])* (r-l)
        max_contain = temp if temp >max_contain else max_contain

        if (height[l]>height[r]):
            r-=1
        else:
            l+=1
    return max_contain


def water_area_executor():
    print("water area")
    print(water_area([1,8,6,2,5,4,8,3,7])) # 49
    print(water_area([1,1])) # 1
    