# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 
# Example 1:
# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Example 3:
# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 
# Constraints:
# 3 <= arr.length <= 5 * 104
# -104 <= arr[i] <= 104

# Approach:

# If total sum of the array is not divisible by 3, then return False. 
# Calculate the partition sum each subarray must adhere to. If the cumulative sum at the current index meets the partition sum, then 
# we reset the cumulative sum to zero. Increase the partition count by 1. If by end, the partition count >= 3, then return 3. Else return False.

# The reason we dont check it is exactly equal to 3 is because of the edge case : [0,0,0,0] expects true. Here, the count will be 4 but satisfies the condition.


def partition_three_parts(arr):

    total_sum = sum(arr)

    if total_sum % 3 != 0:
        return False
    
    cumulative_sum, partition_sum, count = 0, total_sum // 3, 0

    for num in arr:
        cumulative_sum += num
        if cumulative_sum == partition_sum:
            cumulative_sum = 0
            count += 1
    
    return count >= 3


# Time Complexity:
# O(N) where N is the total number of elements in the array.
# Space Complexity:
# O(1) constant space

# Tests:
# command: python test_partition_3_parts.py
