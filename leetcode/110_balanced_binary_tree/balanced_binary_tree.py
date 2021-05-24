# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

def is_balanced(self, root):

    def get_depth(node):
        if not node:
            return 0
        return 1 + max(get_depth(node.left), get_depth(node.right))

    if not root:
        return True
    
    return abs(get_depth(root.left) - get_depth(root.right)) <= 1 and (self.is_balanced(root.left) and self.is_balanced(root.right))


# Time Complexity:
# O(N) where N is the number of nodes in a tree.

# Space complexity: 
# O(N), The recursion stack may go up to O(N) if the tree is unbalanced.