# Given the reference to the root of a binary tree, and a target value, remove all the leaf nodes that contain the target and return the modified tree.
# Note: If you remove a leaf node that contains the target value and the parent node now becomes a leaf with a value of target, you must remove the parent as well.

# Ex: Given the following binary tree and target…
#       1
#      / \
#     2   3
#    /
#   2, target = 2, return the tree modified as follows...
#        1
#         \
#          3

# Approach:

# To solve this problem, we can leverage recursion and perform a depth-first search on our tree. During every one of our recursive calls, 
# we can check if our root.left is not null. If it’s not, we can set the left subtree equal to the result of our recursive call that will remove 
# all leaf nodes that contain target. Similarly, we can also have the same check for our root.right to ensure that we also remove all nodes that are 
# leaf nodes that contain target from our entire right subtree. Once both of these recursive calls return, we can check whether or not the current node 
# should be removed by checking if both children are now null and if root.val is equal to our target. If both these conditions are tree, we should return null 
# to remove the node itself and root otherwise. Once our top level recursive call has returned, we will have modified our tree as asked.

def remove_leaves_with_target(root, target):

    if root.left:
        root.left = removeLeavesWithTarget(root.left, target)
    
    if root.right:
        root.right = removeLeavesWithTarget(root.right, target)
    
    return None if root.left == root.right and root.val == target else root


# Time Complexity:
# O(N) where N is the total number of nodes in a tree.
# Space Complexity:
# O(H) where H is the height of the tree(log N in case of complete binary tree else O(N) in a skewed binary tree)



