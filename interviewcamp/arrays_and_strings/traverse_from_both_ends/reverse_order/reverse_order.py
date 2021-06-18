# Given an array reverse the order of its elements. For ex: [1,3,6,112,4] -> [4, 112, 6, 3, 1]

# Approach:
# Two pointer approach - Keep one pointer at the beginning of the array and the other one at the end. 
# Swap elements in these indexes and repeat the process by moving the forward pointer ahead and the pointer from the back towards 
# the beginning until they dont cross each other.

def reverse_order_array(nums):
    if not nums:
        return nums
    
    front, back = 0, len(nums) - 1

    while front < back:
        nums[front], nums[back] = nums[back], nums[front]
        front  += 1
        back -= 1
    
    return nums


# Time complexity:
# O(N) as we need to traverse the entire array.

# Space complexity:
# O(1) as no extra space used.

# Test command:
# python test_reverse_order.py