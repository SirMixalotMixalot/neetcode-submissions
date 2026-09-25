class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0]) # sort by start
        nonoverlap = [intervals[0]]
        [start, end] = intervals[0]
        j = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] <= end and intervals[i][1] > end:
                nonoverlap[j][1] = intervals[i][1]
                end = intervals[i][1]
            elif intervals[i][0] > end: # new non overlapping
                nonoverlap.append(intervals[i])
                start = intervals[i][0]
                end = intervals[i][1]
                j += 1
        return nonoverlap 
                

        