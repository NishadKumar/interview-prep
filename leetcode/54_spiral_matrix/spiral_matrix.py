# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Approach:

# We track 4 pointers namely top, left, right and bottom. We move these according to the spiral order mentioned. When we meet the total number of elements in the 
# matrix originally, that indicates we are done.

def spiral_order(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        
        total_elements = rows * cols
        
        left, top = 0, 0
        right, bottom = cols - 1, rows - 1
        
        while len(result) != total_elements:

            #move from left to right on top
            for i in range(left, right + 1):
                if len(result) != total_elements:
                    result.append(matrix[top][i])
                    
            top += 1
            
            #move from top to bottom on right
            for i in range(top, bottom + 1):
                if len(result) != total_elements:
                    result.append(matrix[i][right])
            
            right -= 1
            
            #move from right to left on bottom
            for i in range(right, left - 1, -1):
                if len(result) != total_elements:
                    result.append(matrix[bottom][i])
            
            bottom -= 1
            
            #move from bottom to top on left
            for i in range(bottom, top - 1, -1):
                if len(result) != total_elements:
                    result.append(matrix[i][left])
            
            left += 1
        
        return result


# Time complexity:
# O(M * N) - To traverse each cell in matrix of M rows and N cols.

# Space Complexity:
# O(1) - No extra space used.