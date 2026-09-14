class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for [a, b] in prerequisites:
            preqs[a].append(b) # b is a prereq to a

        # built graph. now we dfs on each path and if it was already seen on our visited path, its a cycle, otherwise, continue
        visited = set() # do not explore branches we have already searched
        visiting = set()

        def dfs(node): # returns whether we found a cycle
            if node in visited:
                return False
            visiting.add(node)
            visited.add(node)
            for course in preqs[node]:
                if course in visiting:
                    return True # this course was on our path
                if dfs(course):
                    return True
            visiting.remove(node)
            return False
        
        for c in range(numCourses):
            if dfs(c):
                return False
        return True


        