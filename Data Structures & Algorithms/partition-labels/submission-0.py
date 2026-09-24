class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        ps = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c])

            if i == end:
                ps.append(size)
                size = 0
        return ps



        