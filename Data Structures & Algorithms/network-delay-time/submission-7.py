import heapq
import math
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = defaultdict(lambda: math.inf)
        nodesAfter = defaultdict(list)
        for [u, v, t] in times:
            nodesAfter[u].append((v, t))
        dist[k] = 0
        heap = [(0, k)]
        seen = set()
        while heap:
            (t, node) = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            for (nd, c) in nodesAfter[node]:
                if t + c < dist[nd]:
                    dist[nd] = t + c
                    heapq.heappush(heap, (t + c, nd))
        maxSoFar = -1
        for i in range(1, n + 1):
            if i not in seen:
                return -1
            print(maxSoFar, i, n)
            maxSoFar = max(dist[i], maxSoFar)
        return maxSoFar
            




        