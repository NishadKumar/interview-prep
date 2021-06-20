# Problem:
# You are given an array of integers. Rearrange the array so that all zeroes are at the end of the array.
# Note: Keep non-zero elements in order
# For example, [4, 2, 0, 1, 0, 3, 0] -> [4, 2, 1, 3, 0, 0, 0]

# Approach:
# 2-pointer intuitive approach. One pointer to scan each element and the other pointer to basically indicate where the next encountered zero should sit.

def move_zeroes(nums):
    if not nums:
        return nums
    
    left, right = 0, 0

    while left < len(nums):
        if nums[left] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
        left += 1
     
    return nums



# Time Complexity: 
# O(N) - As we scan all elements of the array.
# O(1) - As no extra space is utilized. 


# Tests:
# command: python test_move_zeroes_end.py