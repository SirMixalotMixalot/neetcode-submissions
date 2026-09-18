class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for [a,b] in prerequisites:
            preqs[a].append(b)
        
        visited = set()
        visiting = set()

        def hasCycle(course):
            if course in visited:
                return False
            if course in visiting:
                return True
            
            visiting.add(course)
            for p in preqs[course]:
                if hasCycle(p):
                    return True
            visited.add(course)
            visiting.remove(course)
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True
        