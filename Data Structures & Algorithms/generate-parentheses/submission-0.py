class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(curr, op, cls):
            if op > cls:
                return # nonesense
            if op == cls == 0:
                ans.append(curr[:])
                return
            if op >= 1:
                curr += "("
                dfs(curr, op -1, cls)
                curr = curr[:-1]
                curr += ")"
                dfs(curr, op, cls - 1)
            else:
                curr += ")"
                dfs(curr, op, cls - 1)
            curr = curr[:-1]
        dfs("", n, n)
        return ans

        