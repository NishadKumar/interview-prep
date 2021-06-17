# Given an array of numbers, replace each even number with twoof the same number. e.g, [1,2,5,6,8, , , ,] -> [1,2,2,5,6,6,8,8].
# Assume that the array has the exact amount of space to accommodate the result.


# Approach:
# 2 pointers - one for moving along the array from left to right and the other from the end of the array to begin filling up the even numbers found. 

def reverse_traversal_array(nums):

    if not nums:
        return nums
    
    end = len(nums) - 1
    i = get_last_number(nums)

    while i >= 0:
        if nums[i] % 2 == 0:
            nums[end] = nums[i]
            end -= 1
        nums[end] = nums[i]
        end -= 1
        i -= 1
    
    return nums

def get_last_number(nums):
    index = len(nums) - 1

    while index >= 0 and nums[index] == -1:
        index -= 1
    
    return index

# Time Complexity: 
# O(N) - As we move along each element of the array.
# O(1) - As no extra space is utilized. 


