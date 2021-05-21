# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.

# Example 1:
# Input: [1,1,1,1,1,null,1]
# Output: true

# Example 2:
# Input: [2,2,2,5,2]
# Output: false

# Approach:

# To determine if a subtree is univalued:
# a) Recursively traverse all the nodes in the tree. If you arrive at null, that means its a leaf node, which is unival by default. 
# b) If the right univalued subtree's root val is not equal to current root node val, return False
# c) If the left univalued subtree's root val is not equal to current root node val, return False
# d) return True if left and right both subtrees are univalued provided their root values are equal to current root node val.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def is_unival_tree(self, root: TreeNode) -> int:
            """
            :type root: TreeNode
            :rtype: bool
            """
            if not root:
                return True
            
            if root.left and root.left.val != root.val:
                return False
            
            if root.right and root.right.val != root.val:
                return False
            
            if self.is_unival_tree(root.left) and self.is_unival_tree(root.right):
                return True
            
            return False


# Time Complexity:
# Since we have to traverse through all the nodes once, it is O(N).

# Space Complexity:
# It is the maximum depth of a binary tree: O(log N)