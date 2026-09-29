"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort both start and end time into 2 arrays
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s, e = 0, 0
        count = 0
        res = 0
        while s < len(starts) and e < len(ends):
            if ends[e] > starts[s]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res
