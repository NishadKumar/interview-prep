# Given a binary array (i.e. an array containing only zeroes and ones), bits, return the length of the longest streak of ones after deleting one element from the given bits.

# Ex: Given the following bits…
# bits = [0, 1, 1, 0, 1], return 3.

# Ex: Given the following bits…
# bits = [1, 1, 1, 1, 1], return 4.

# To solve this problem, we need to keep track of two things. First, our current count for consecutive ones and second, the previous count of consecutive ones. 
# We can iterate through our bits incrementing our current count each time we find a one. If we ever encounter a zero, we must update our longestto be the maximum 
# between its current value and the sum of our count plus our previous count. Now that we’ve updated our longest, we can set our previous to be our count 
# (since our current count just ended) and reset our count to be zero. Once our loop ends, we can update our longest one more time and then return either our 
# longest or our longest minus one (i.e. in the even that all bits were a one we still need to remove a bit).

def one_bits(bits):

    previous_streak = 0
    current_streak = 0
    longest_streak = 0

    for bit in bits:
        if bit:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, previous_streak + current_streak)
            previous_streak = current_streak
            current_streak = 0
    
    longest_streak = max(longest_streak, previous_streak + current_streak)
    return longest_streak - 1 if longest_streak == len(bits) else longest_streak

# Time Complexity:
# O(N) to traverse the array
# Space Complexity:
# O(1) as no extra space used