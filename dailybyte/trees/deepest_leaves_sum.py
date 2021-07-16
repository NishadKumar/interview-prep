# Given the reference to the root of a binary tree, return the sum of all leaves at the deepest level.

# Ex: Given the following tree…
#       2
#      / \
#     4   5, return 9 (4 and 5 are at the deepest level and sum to 9).

# Ex: Given the following tree…
#       1
#        \
#         2
#          \
#           3, return 3.

#Approach: 
# To solve this problem, we can use a breadth-first search. We can traverse our tree level by leveling constantly summing all nodes’ values on the current level. 
# By recalculating this sum at every single level, we’re guaranteed that the last level we sum together is the sum to return as our answer 
# (since the last level we sum is guaranteed to be at the deepest level in the tree).

def deepest_leaves_sum(root):

    if not root:
        return 0
    
    queue = [root]

    while queue:
        current_level_sum = 0

        for i in range(len(queue)):
            node = queue.pop(0)
            current_level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
    return current_level_sum

# Time Complexity:
# O(N ) to visit each node.

# Space complexity: 
# Up to O(N) to keep the queue. Let's use the last level to estimate the queue size. 
# This level could contain up to O(N/2) tree nodes in the case of complete binary tree.