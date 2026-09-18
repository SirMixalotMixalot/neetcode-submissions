import math
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = defaultdict(lambda: math.inf)
        dist[k] = 0
        nextNodes = defaultdict(list)
        for [u,v,t] in times:
            nextNodes[u].append((t, v))
        heap = [(0, k)]
        seen = set()
        while heap:
            d, curr = heapq.heappop(heap)
            if curr in seen:
                continue
            seen.add(curr)
            for t, child in nextNodes[curr]:
                if d + t < dist[child]:
                    dist[child] = d + t
                    heapq.heappush(heap, (d + t, child))
        m = -1
        for node in range(1, n + 1):
            if node not in seen:
                return -1
            m = max(m, dist[node])
        return m

            


        