class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # find out if you can finish, if we can finish, topological sort and then add in order of increasing outdegree
        if not self.canFinish(numCourses, prerequisites):
            return []
        # topological sort, its a dag
        degrees = defaultdict(int)
        classesAfter = defaultdict(list)
        for [a,b] in prerequisites:
            classesAfter[b].append(a)
            degrees[a] += 1
        q = []
        for c in range(numCourses):
            if degrees[c] == 0:
                q.append(c)
        res = []
        while q:
            curr = q.pop()
            res.append(curr)
            for child in classesAfter[curr]:
                degrees[child] -= 1
                if degrees[child] == 0:
                    q.append(child)
        if len(res) == numCourses:
            return res
        else:
            return []

        
        
    
    def canFinish(self, numCourses, prerequisites):
        preqs = defaultdict(list)
        for [a, b] in prerequisites:
            preqs[a].append(b)
        
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            for child in preqs[node]:
                if dfs(child):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False
        for c in range(numCourses):
            if dfs(c):
                return False
        return True
        