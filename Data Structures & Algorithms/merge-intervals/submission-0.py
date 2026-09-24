class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda intervals : intervals[0])

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            lastEnd = output[-1][1]

            if lastEnd >= intervals[i][0]:
                output[-1][1] = max(lastEnd, intervals[i][1])
            else:
                output.append(intervals[i])

        return output
        
        