#Problem:

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 
# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


#Approach:
# As it is clear from the problem, we need to use a graph to solve this. And since the problem is particular about a course dependent on another course, 
# we can conclude using DAGs(Directed Acyclic Graphs) is the way to go ahead. Also, if there exists a cycle, it is impossible to finish all the courses since
# one will never know which course to take first. The problem entirely boils down to whether there exists a cycle in the DAG. We return true if there are no cycles.
# Else we return false.

# Adjacency matrix helps us represent this graph. For every course, we will have the list of courses it depends on. We do a depth first search to all its connected
# courses. If in case we come across a course we had in the queue to process, that means there is a cycle. And we can return False immediately. Else we continue and 
# mark the current course as processed. 

import collections

def can_finish(num_courses, prerequisites):
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
        return False
        
    visited = collections.defaultdict(int)
    graph = collections.defaultdict(list)
    
    for u,v in prerequisites:
        graph[u].append(v)
    
    for i in range(num_courses):
        if has_cycle(i):
            return False
    
    return True
    
    #Time Complexity:
    # O(M  + N) -> where M is the number of dependencies, N is the number of courses. 
    # For example: In the worst case scenario, we take O(M) to build the adjacency graph and O(N) time to cover all dependencies. 

    #Space Complexity:
    # O(M + N) -> Same explanation as above as we need to store max of M dependencies in graph and N courses to check if visited or not.

    # Tests:
    # command: python test_course_schedule.py