# You are given a two-dimensional matrix containing only ones and zeroes representing a computer network. 
# Every one in the matrix represents a server and every zero represents an empty space. 
# Two servers within the network can communicate if they are either in the same row or the same column. 
# Return the total number of servers that can communicate with at least one other server.

# Example 1:
# matrix = [
#   [1, 0],
#   [1, 0],
# ], return 2 (both servers are in the same column and can therefore communicate with one another).

# Example 2:
# matrix = [
#   [1, 0],
#   [0, 1],
# ], return 0.

# Approach:
# To solve this problem, we can keep track of two things, first the number of servers in each row and second the number of servers in each column. 
# To do this, we will leverage two arrays, rows and cols. With our arrays initialized, we can now start iterating through our matrix. 
# For every element we traverse, we can check if it is a server (i.e. a one). If it is, we can increment the server count for the current row and the current column.
# Once we have done an initial sweep through or matrix recording the total number of servers in each row and column, we can iterate through our matrix a second time. 
# This time, for each server (i.e. one) we find, we can check if there is another server within the current row or the current column that the server we are on can communicate with (i.e. rows[i] > 1 || cols[j] > 1). 
# If there is, we can increment our servers count by one. Once we finish iterating through our matrix a second time, we can return our servers count.

def computer_network(matrix):

    total_servers = 0

    if not matrix:
        return total_servers
    
    rows = [0] * len(matrix)
    cols = [0] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                rows[i] += 1
                cols[j] += 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                total_servers += 1
    
    return total_servers


# Runtime: O(N x M) where N is the total number of rows in our matrix and M is the total number of columns in our matrix.
# Space complexity: O(N + M) where N is the total number of rows in our matrix and M is the total number of columns in our matrix.