#Problem: 
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

# Approach:

# Sliding window technique. Maintain left and right pointer. Right pointer moves along until the end of array while the left pointer remains fixed to calculate
# the maximum consecutive ones. 


def longest_ones(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        max_ones, zero_count = 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
               if nums[left] == 0:
                   zero_count -= 1
               left += 1

            max_ones = max(max_ones, right - left + 1)
        
        return max_ones

#Time Complexity:
# O(N) - Worst case it leads to sliding window from left most element to right most element.

#Space Complexity:
# O(1) - Constant space.

# Tests:
# command: python test_max_consecutive_ones_3.py

