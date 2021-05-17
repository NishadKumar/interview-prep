# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]

# Approach:
# Same as course schedule part 1. Except we will add the course to the maintained order list once the course is marked processed. 


import collections

def find_order(num_courses, prerequisites):
    """
    :type num_courses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    
    def has_cycle(course):
        
        # -1 for processing the current course
        # 1 to mark current course processed
        
        #cycle found
        if visited[course] == -1:
            return True
        
        #already processed course
        if visited[course] == 1:
            return False
        
        #mark course as processing, explore neighbors
        visited[course] = -1
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        
        #mark current course as processed
        visited[course] = 1
        order.append(course)
        return False
        
    visited = collections.defaultdict(int)
    graph = collections.defaultdict(list)
    order = []
    
    for u,v in prerequisites:
        graph[u].append(v)
    
    for i in range(num_courses):
        if has_cycle(i):
            break
    
    return order if len(order) == num_courses else []
    
#Time Complexity:
# O(M  + N) -> where M is the number of dependencies, N is the number of courses. 
# For example: In the worst case scenario, we take O(M) to build the adjacency graph and O(N) time to cover all dependencies. 

#Space Complexity:
# O(M + N) -> Same explanation as above as we need to store max of M dependencies in graph and N courses to check if visited or not.

# Tests:
# command: python test_course_schedule_2.py