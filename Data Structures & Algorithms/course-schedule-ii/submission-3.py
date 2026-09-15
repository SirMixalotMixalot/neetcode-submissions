from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort, if len(res) != numCourses, there was a cycle
        classesAfter = defaultdict(list)
        indegree = defaultdict(int)
        for [a, b] in prerequisites:
            classesAfter[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        res = [] # our answer
        while q:
            curr = q.popleft()
            res.append(curr)
            for child in classesAfter[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child) # enqueue completed node
        if len(res) < numCourses:
            return []
        
        return res

        
        