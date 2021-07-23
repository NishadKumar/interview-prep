# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. 
# If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. 
# More formally, the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.

# Example 1:
# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.


# Example 2:
# Input: root = [2,2,2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 25].
# 1 <= Node.val <= 231 - 1
# root.val == min(root.left.val, root.right.val) for each internal node of the tree.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach:
# When traversing the tree at some node, node, if node.val > min1, we know all values in the subtree at node are at least node.val 
# so there cannot be a better candidate for the second minimum in this subtree. Thus, we do not need to search this subtree.

# Also, as we only care about the second minimum ans, we do not need to record any values that are larger than our current candidate for the second minimum, 
# so unlike Approach #1 we can skip maintaining a Set of values(uniques) entirely.

def second_minimum_value(self, root):
    self.answer = float('inf')
    current_minimum = root.val

    def dfs(node):
        if node:
            if current_minimum < node.val < self.answer:
                self.answer = node.val
            elif node.val == current_minimum:
                dfs(node.left)
                dfs(node.right)
    
    dfs(root)
    return self.answer if self.answer < float('inf') else -1

# Time Complexity:
# O(N), where N is the total number of nodes in the given tree. We visit each node at most once.

# Space Complexity:
# O(N). The information stored in ans and min1 is O(1), but our depth-first search may store up to O(h) = O(N) information in the call stack, 
# where h is the height of the tree.

