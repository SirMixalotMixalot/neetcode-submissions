class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        completeable = True
        deps = defaultdict(list)
        for [ai,bi] in prerequisites:
            deps[bi].append(ai)

        seen = set()
        visited = set()
        def dfs(currNode):
            nonlocal completeable, seen
            if not completeable:
                return
            if currNode in visited:
                return
            if currNode in seen:
                completeable = False
                return
            seen.add(currNode)
            for child in deps[currNode]:
                dfs(child)
            seen.remove(currNode)
            visited.add(currNode)
        for c in range(numCourses):
            if not completeable:
                break
            dfs(c)

        return completeable