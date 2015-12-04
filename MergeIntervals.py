# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n < 2:
            return intervals

        intervals = sorted(intervals, key = lambda intervals: intervals.start)
        i = 0
        j = 1
        curr = 0
        while j < n :
                
            while intervals[i].end >= intervals[j].start:
                if intervals[i].end <= intervals[j].end:
                    intervals[i].end = intervals[j].end
                    
                j += 1
                if j == n:
                    curr += 1
                    break
            
            i = j
            curr += 1
            j += 1
            print i,j,curr, intervals
        return intervals[:curr]
            
                
            
            
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n < 2:
            return intervals

        intervals = sorted(intervals, key = lambda intervals: intervals.start)
        result = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1].end >= interval.start:
                if result[-1].end <= interval.end:
                    result[-1].end = interval.end
            else:
                result.append(interval)
        return result
        
            
            
            