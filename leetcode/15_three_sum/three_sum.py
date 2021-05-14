#Problem:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []

# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

#Approach:

# Brute force:
# Calculate sum of every 3 possible combinations of numbers. Select those who sum to 0. Remove duplicates(needs a hashset). Complex code.

# Optimized approach:
# Sort array initially. For every element in array call 2sum approach to find its complement in the rest of the array elements to equal 0.



def three_sum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    #to exclude duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    #to exclude duplicates                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return result

#Time Complexity:
# O(N^2) + O(N Log N) => O(N^2) 
# O(N) for finding two sum, getting called N times.

#Space Complexity:
# O(N) -> worst case for quick sort

# Tests:
# command: python test_three_sum.py