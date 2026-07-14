"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i]
            i2 = intervals[i-1]

            if i2.end > i1.start:
                return False
        return True