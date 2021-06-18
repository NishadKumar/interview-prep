# Given a sorted array of integers, find two numbers in the array that sum to a given target.
# For example: if a = [1,2,3,5,6,7], target = 11, answer will be [5,6]

# If no such pair exists, return [-1, -1]
# Assumption: Only 1 valid pair exists as a solution.

def two_sum_target(nums, target):
    if not nums:
        return nums

    front, back = 0, len(nums) - 1

    while front < back:
        if nums[front] + nums[back] == target:
            return [nums[front], nums[back]]
        elif nums[front] + nums[back] < target:
            front += 1
        else:
            back -= 1
    
    return [-1, -1]

# Time complexity:
# O(N) as we need to traverse the entire array.

# Space complexity:
# O(1) as no extra space used.

# Test command:
# python test_two_sum.py