from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # find out if you can finish, if we can finish, topological sort and then add in order of increasing outdegree
        # topological sort, its a dag
        degrees = defaultdict(int)
        classesAfter = defaultdict(list)
        for [a,b] in prerequisites:
            classesAfter[b].append(a)
            degrees[a] += 1
        q = deque()
        for c in range(numCourses):
            if degrees[c] == 0:
                q.append(c)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for child in classesAfter[curr]:
                degrees[child] -= 1
                if degrees[child] == 0:
                    q.append(child)
        if len(res) == numCourses:
            return res
        else:
            return []
        