# Given two string arrays, word1 and word2, return whether or not the two arrays represent the same string.

# Ex: Given the following word1 and word2…

# word1 = ["abc", "d"], word2 = ["ab", "cd"], return true.
# Ex: Given the following word1 and word2…

# word1 = ["a", "b", "c"], word2 = ["a", "b", "d"], return false.


# Approach:
# To solve this problem, we can use a “two” pointer technique although we’ll actually be using four pointers. 
# These four pointers will consist of w1, w2, i, and j, which will be responsible for the word within words1 that we’re on, the word within words2 that we’re on, 
# the letter within the current string within word1 that we’re on and the letter within the current string within word2 that we’re on respectively. 
# All of our pointers will initially start at zero, and then we can begin iterating through our words and characters, while we have not traversed every word within 
# word1 and word2. At every iteration of our loop, we can first check if the two characters within each of our words are the same. 
# If they’re not, we can return false immediately. If they are, we can check for each of our pointers, i and j, if they’ve reached the last character of the current word within
# their respective arrays. If they have, we can increment w1 and/or w2 for our respective arrays, 
# and reset our i and/or j to zero so that we start at the first character of the next word. If we have not reached the end of our word, we only need to increment i/j. 
# Once our loop ends, we can return whether or not our w1 and w2 pointers both reached the lengths of their respective arrays.

def check_strings(word1, word2):
    if not word1 or not word2:
        return False
    
    i, j = 0, 0
    w1, w2 = 0, 0

    while w1 < len(word1) and w2 < len(word2):

        if word1[w1] != word2[w2]:
            return False
        
        if i == len(word1[w1]) - 1:
            i = 0
            w1 += 1
        else:
            i += 1
        
        if j == len(word2[w2]) - 1:
            j = 0
            w2 += 1
        else:
            j += 1
        
    return w1 == len(word1) and w2 == len(word2)


# Time Complexity:
# O(M + N) where M = length of word1 array and N = length of word2 array.

# Space complexity:
# O(1) as it is done in place. 