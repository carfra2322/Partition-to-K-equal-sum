'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

nums = [4, 3, 2, 3, 5, 2, 1]
k=4




def sublist(lst,target_value):
    nums = lst
    nums.sort(reverse=True)
    temp_target = 0
    temp_list = []
    position = [x for x in range(len(nums))]
    for i in range(len(nums)):
        if(temp_target<target_value and i in position):
            temp_target+=nums[i]
            position.remove(i)
            if(temp_target>target_value):
                temp_target-=nums[i]
                position.append(i)
        #print(target)
        #print(position)
        #print(nums)

    for i in position:
        temp_list.append(nums[i])
            #print(nums[i])
    #print(temp_list)
    return temp_list

def callfunction(nums, k):
    if(sum(nums)%k>0):
        return False
    target_value = int(sum(nums)/k)
    #print("target value", target_value)
    temp = sublist(nums, target_value)
    for i in range(len(nums)):
        temp = sublist(temp, target_value)
    if(len(temp)>0):
        return False
    else:
        return True

callfunction(nums, k)
