# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

# Example 1:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]
# Explanation: The ranges are:
# [2,2] --> "2"
# [4,49] --> "4->49"
# [51,74] --> "51->74"
# [76,99] --> "76->99"

# Example 2:
# Input: nums = [], lower = 1, upper = 1
# Output: ["1"]
# Explanation: The only missing range is [1,1], which becomes "1".

# Example 3:
# Input: nums = [], lower = -3, upper = -1
# Output: ["-3->-1"]
# Explanation: The only missing range is [-3,-1], which becomes "-3->-1".

# Example 4:
# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing numbers.

# Example 5:
# Input: nums = [-1], lower = -2, upper = -1
# Output: ["-2"]

# Approach:
# Linear Scan -> 
# Since the input array, nums, is sorted ascendingly and all the elements in it are within the given [lower, upper] bounds, we can simply check consecutive elements to see if they differ by one or not. If they don't, then we have found a missing range.

# When nums[i] - nums[i-1] == 1, we know that there are no missing elements between nums[i-1] and nums[i].
# When nums[i] - nums[i-1] > 1, we know that the range of elements, [nums[i-1] + 1, nums[i] - 1], is missing.

# However, there are two edge cases:

# Edge case 1: If we don't start with lower as the first element of the array, we will need to include [lower, num[0] - 1] as a missing range as well.

# Edge case 2: Similarly, if we don't end with upper as the last element of the array, we will need to include [nums[n-1] + 1, upper] as a missing range as well. 
# Note n here is the length of the input array, nums.


def find_missing_ranges(nums, lower, upper):

    def format_ranges(lower, upper):
        if lower == upper:
            return str(lower)
        return str(lower) + "->" + str(upper)
    

    result = []
    previous = lower - 1

    for i in range(len(nums) + 1):
        current = nums[i] if i < len(nums) else upper + 1

        if previous + 1 <= current - 1:
            result.append(format_ranges(previous + 1, current - 1))
        
        previous = current
    
    return result

# Time Complexity:
# O(N) where N is length of nums

# Space Complexity:
# O(1) as no extra space is needed for computation. 

# Tests:
# python test_missing_ranges.py

