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
        if not intervals or not newInterval:
            return intervals or newInterval
        s = newInterval.start
        e = newInterval.end
        left, right = [],[]
        for i in intervals:
            if i.end < s:
                left += i
            elif i.start > e:
                right += i
            else:
                s = min(s,i.start)
                e = max(e,i.end)

        return left + [Interval(s,e)]+right


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals or not newInterval:
            return intervals or [newInterval]
        s = newInterval.start
        e = newInterval.end
        l, r = 0,len(intervals)
        for i in intervals:
            if i.end < s:
                l += 1
            elif i.start > e:
                r -= 1
            else:
                s = min(s,i.start)
                e = max(e,i.end)

        return intervals[:l] + [Interval(s,e)]+intervals[r:]

