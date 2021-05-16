# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

def merge(intervals):

    merged = []
    intervals = intervals.sort(key = lambda interval: interval[0])

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


#Time Complexity:
# O(N^2) to sort using quick sort as worst case.
# O(N log N) to sort using merge sort as worst case.

#Space Complexity:
# O(log N) for quick sort, O(N) for merge sort.

# Tests:
# command: python merge_intervals.py