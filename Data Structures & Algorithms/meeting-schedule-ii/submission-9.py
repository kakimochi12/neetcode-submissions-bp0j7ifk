"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in range(len(intervals)):
            time.append([intervals[i].start, 1])
            time.append([intervals[i].end, -1])
        
        time.sort(key = lambda x:(x[0], x[1]))
        count = 0
        res = 0

        for t in time:
            count += t[1]
            res = max(res, count)
        return res