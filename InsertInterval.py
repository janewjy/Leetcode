# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not newInterval or not intervals:
            return intervals or [newInterval]
        n = len(intervals)
        start, i = 0,0
        if intervals[0].start > newInterval.end:
            return [newInterval] + intervals
        while i < n:
            if intervals[i].end >= newInterval.start:
                newInterval.start = min(newInterval.start, intervals[i].start )
                break
            i += 1
        if i == n:
            intervals.append(newInterval)
            return intervals
        start = i

        while i < n:
            if intervals[i].start > newInterval.end:
                break
            i += 1
        newInterval.end = max(newInterval.end, intervals[i-1].end)

        end = i
        
        intervals = intervals[:start] + [newInterval] + intervals[end:]
        return intervals
        

        

[[1,5]]
[2,3]

[[1,5]]
[0,3]

[[1,5]]
[0,0]