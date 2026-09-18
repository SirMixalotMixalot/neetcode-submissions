from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort, get degrees of courses
        coursesAfter = defaultdict(list)
        indegree = defaultdict(int)
        for [a,b] in prerequisites:
            coursesAfter[b].append(a)
            indegree[a] += 1
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        res = []
        while q:
            curr = q.popleft()
            res.append(curr) # processed
            for c in coursesAfter[curr]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        if len(res) != numCourses:
            return []
        return res


        