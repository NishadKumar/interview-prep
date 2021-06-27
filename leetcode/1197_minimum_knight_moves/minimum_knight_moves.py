# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
# A knight has 8 possible moves it can make. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

# Example 1:
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] -> [2, 1]

# Example 2:
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] -> [2, 1] -> [4, 2] -> [3, 4] -> [5, 5]
 
# Constraints:
# |x| + |y| <= 300

# Approach: 
# BFS -> This problem boils down to finding shortest path from knight's origin to its destination. Dijkstra's algorithm is the most intuitive 
# approach one can think of. We start by queueing the origin and explore all the initial knight's possible directions. If we reach the vertex we 
# are looking for, we are done. Else, we repeat the process until we find it. Mind to have a data structure to not visit the already explored vertex.
# A set can be used for that. Also, a queue to process vertex in order helps us achieve the task. 

def min_moves(x, y):

    offsets = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
    
    def bfs(x, y):

        queue = [(0, 0)]
        visited = set()
        steps = 0

        while queue:
            current_level_length = len(queue)

            for i in range(current_level_length):
                current_x, current_y = queue.pop(0)
                if (current_x, current_y) == (x, y):
                    return steps

                for offset_x, offset_y in offsets:
                    next_x, next_y = current_x + offset_x, current_y + offset_y
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))

            steps += 1
                    
    return bfs(x, y)

# Time & Space Complexity:
# If you have premium subscription on leetcode, then I would recommend reading the article by the author. 

# Tests:
# python test_minimum_knight_moves.py
