# Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
# Note:

# s will consist of lowercase letters and have length in range [1, 500]

# Approach:
# We place characters sorted based on decreasing frequency next to each other. In the end, we will surely have a character whose count could be >= 1. If count is 1
# we can make it work else, the solution is not possible and we return "".

import heapq

def reorganize_string(s):

    dictionary = {}
    result = ''

    for character in s:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
    
    max_heap = [(val, key) for key, val in dictionary.items()]
    heapq._heapify_max(max_heap)

    while len(max_heap) > 1:
        current_char = heapq.heappop(max_heap)[1]
        next_char = heapq.heappop(max_heap)[1]

        result += current_char
        result += next_char

        dictionary[current_char] -= 1
        dictionary[next_char] -= 1

        if dictionary[current_char] > 0:
            heapq.heappush(max_heap, (dictionary[current_char], current_char))
        
        if dictionary[next_char] > 0:
            heapq.heappush(max_heap, (dictionary[next_char], next_char))
        
    if max_heap:
        last_char = heapq.heappop(max_heap)[1]
        if dictionary[last_char] > 1:
            return ''
        result += last_char

    return result
        

#Time Complexity:
# O(N log N) -> Call heapify N times for log N levels at max.
#Space Complexity:
# O(N) -> Dictionary space to hold all characters in s

# Tests:
# command: python test_reorganize_string.py