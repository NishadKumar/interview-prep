# Given the root of two binary trees, a and b, return the resulting tree when you overlay a on top of b.
# Note: For any nodes that overlap a is placed on top of b, the resulting tree’s node should contain their sum.

# Ex: Given the following a and b…

# a = 1     b = 4
#    / \       / \
#   2   3     5   6, return the resulting tree...
#            5 (1 + 4)
#          /   \
# (2 + 5) 7     9 (3 + 6)
# Ex: Given the following a and b…

# a = 7     b = 9
#    / \       /
#   2   1     5, return the resulting tree...
#          16
#         /  \
#        7    1

#Approach:
# To solve the problem, we can traverse each node in both of our trees summing appropriate values. 
# We can start from each of their roots and work our way down the tree. A simple way to do this is with recursion. 
# At every one of our recursive calls we can first check how many nodes we have. 
# If both a and b are null, we have no nodes to process and can return null. 
# If this is not the case but a is null, we can simply return b and we have one node to process (i.e. b). 
# Similarly, if b is null, we can return a and have one node to process (i.e. a). Otherwise, we have two nodes to process, a and b. 
# To process them, we can create a new node that will represent the start of our new tree (the first time we enter the else block) called root and 
# we can set root’s value to be the sum of a.val plus b.val since we know we have two nodes. Then, we can set root.left equal to the result of 
# the recursive call of our left subtrees and set root.right equal to the result of the recursive call of our right subtrees. 
# Once our recursive calls return and we’ve set both root.left and root.right we can return our root.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def overlay_trees(root_a, root_b):

    if not root_a and not root_b:
        return None
    elif not root_a:
        return root_b
    elif not root_b:
        return root_a
    else:
        node = TreeNode(root_a.val + root_b.val)
        node.left = overlay_trees(root_a.left, root_b.left)
        node.right = overlay_trees(root_a.right, root_b.right)
        return node

# Time Complexity:
# O(N + M) where N is the number of nodes in a and M is the number of nodes in b.

# Space complexity: 
# O(max(N, M)) where N is the number of nodes in a and M is the number of nodes in b.