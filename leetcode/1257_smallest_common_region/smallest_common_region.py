# You are given some lists of regions where the first region of each list includes all other regions in that list.

# Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a region X contains itself.

# Given two regions region1, region2, find out the smallest region that contains both of them.

# If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

# It's guaranteed the smallest region exists.

# Example 1:
# Input:
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# Output: "North America"
 

# Constraints:

# 2 <= regions.length <= 10^4
# region1 != region2
# All strings consist of English letters and spaces with at most 20 letters.


# Approach:
# As stated, given regions r1,r2 and r3, if r1 includes r3, it is guaranteed that there is no such r2 that includes r3. So, imagine a tree with unique parent and children.
# The approach is to wire back region1's and region2's to the same parent or lowest common ancestor. Build a mapping of each child region to the parent region via 
# hashmap. Store all parents of region1 in a set. Repeat for region2 until there is a collision. 


def find_smallest_region(regions, region1, region2):

    parent = dict()

    for region in regions:
        for child in region[1:]:
            parent[child] = region[0]
    
    candidates = set([region1])

    while region1 in parent:
        region1 = parent[region1]
        candidates.add(region1)
    
    while region2 not in candidates:
        region2 = parent[region2]
    
    return region2


# Time Complexity:
# O(N) to traverse the dictionary, where N can be the total number of regions.
# Space Complexity:
# O(N) to store parents of each region and set to store region1 parents(which is a subset of the dictionary)

# Tests:
# python test_smallest_common_region.py

