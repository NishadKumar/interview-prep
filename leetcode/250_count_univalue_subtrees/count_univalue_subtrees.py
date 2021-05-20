# Given the root of a binary tree, return the number of uni-value subtrees.

# A uni-value subtree means all nodes of the subtree have the same value.

# Example 1:
# Input: root = [5,1,5,5,5,null,5]
# Output: 4

# Example 2:
# Input: root = []
# Output: 0

# Example 3:
# Input: root = [5,5,5,5,5,null,5]
# Output: 6
 
# Constraints:

# The number of the nodes in the tree will be in the range [0, 1000].
# -1000 <= Node.val <= 1000

# Approach:

# Breaking down the steps:

# Step 1:
# To calculate the total univalued subtrees, one has to add left univalued trees with right univalued trees and the root in itself if it is univalued too.
# Step 2:
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
    def count_univalue_subtrees(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # STEP 1:
        total_count = self.count_univalue_subtrees(root.left) + self.count_univalue_subtrees(root.right)

        if self.is_unival(root.left) and self.is_unival(root.right) and self.is_unival(root):
                total_count += 1

        return total_count
    
    def is_unival(self, node):
        # STEP 2:
        if not node:
            return True
        
        if node.left and node.left.val != node.val:
            return False
        
        if node.right and node.right.val != node.val:
            return False
        
        if self.is_unival(node.left) and self.is_unival(node.right):
            return True
        
# Time Complexity:
# Since we have to traverse through all the nodes once, it is O(N).

# Space Complexity:
# It is the maximum depth of a binary tree: O(log N)