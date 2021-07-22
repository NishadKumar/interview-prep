# Given an array of words, return all strings in words that are a substring of another word.
# Note: The order in which you return the substrings does not matter.


# Example 1: 
# words = ["abc", "a", "b"], return ["a", "b"].

# Example 2: 
# words = ["ab", "ba", "c"], return [].

# Approach: 
# To solve this problem, we can leverage sorting. To start, we can sort our words by their length in ascending order so that the smallest strings 
# are at the beginning of our array. Then, we can iterate through our words, holding the ith word and checking all the subsequence words, 
# to see if any of the following words contain the word we are holding. If one does, we can add the word we are holding to our substrings list and
# break out of our inner loop. Once both of our loops ends, we can return our substrings.

def word_within_words(words):
    substrings = []

    if not words:
        return substrings

    sorted_words = sorted(words, key=len)
    
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] in sorted_words[j]:
                substrings.append(sorted_words[i])
                break
    
    return substrings

# Runtime Complexity: O(N^2) where N is the total number of elements in words.
# Space complexity: O(N) where N is the total number of elements in words.


