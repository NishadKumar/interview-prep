# Given the reference to the root of a binary tree and the reference to the head of a linked list, return whether or not the entire linked list appears as a subpath within the tree.

# Ex: Given the following root and head…
#       root = 1
#             / \
#            2   3
#           /
#          3
#       head = 1 -> 2 -> 3, return true

# Ex: Given the following root and head…
#       root = 4
#             / \
#            2   7
#           /
#          3
#       head = 2 -> 3 -> 4, return false.

# Approach: 
# To solve this problem, we can use a depth-first search. We can recursively traverse both our tree and our linked list checking if values along each node 
# of the respective data structure match. If they do, we can continue traversing to the next node of each structure to compare subsequent values. 
# If they don’t, we can return false meaning the current path we’re traversing does not match. 
# If we ever get to the end of the linked list (i.e. head is null), then we can return true since we’ve found the entire linked list as a path within our tree. 
# Because this path can occur anywhere in our tree, not necessarily starting from our root, we must ensure that we perform a 
# depth-first search from every node in our tree.

def list_in_tree_path(head, root):
    if not head:
        return True
    elif not root: 
        return False
    else:
        return traverse(head, root) or list_in_tree_path(head, root.left) or list_in_tree_path(head, root.right)

def traverse(head, root):
    if not head:
        return True
    elif not root:
        return False
    else:
        return head.val == root.val and (traverse(head, root.left) or traverse(head, root.right))


# Time Complexity:
# O(N^2) where N is the total number of nodes in a tree
# Space Complexity:
# Max(N, M) where N is the total number of nodes in a tree and M is the total number of nodes in the list.

