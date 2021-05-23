# Given a string, s, return the length of the longest substring between two characters that are equal.
# Note: s will only contain lowercase alphabetical characters.

# Ex: Given the following string s
# s = "bbccb", return 3 ("bcc" is length 3).

# Ex: Given the following string s
# s = "abb", return 0.

# Approach:
# To solve this problem we can leverage a hash map. Our hash map can keep track of the last index a specific character has occurred. 
# We can iterate through all the characters in our string s, continuously updating a variable max_length that will hold the length of the longest 
# substring we've found that occurs b/w 2 equal characters. At every iteration of our loop, we can start by first storing the current character 
# that we are on within s. With the current character stored, we can now check if our hash map already contains this character. If it is, that means  
# it has already occurred and therefore we can update our max_length variable to be the maximum between the current value of max_length and our current index i minus the 
# index that the first occurrence of our current character occurred. If our current character is not in our map, we can place it in our map with the current 
# index i that we are on. Once our loop ends, we'll have stored the longest length subarray b/w 2 equal characters in max_length and can simply return it.

def longest_substring_between_characters(s):
    dictionary = {}
    max_length = -1

    for i in range(len(s)):

        if s[i] in dictionary:
            max_length = max(max_length, i - dictionary[s[i]] - 1)
        else:
            dictionary[s[i]] = i
    
    return max_length
