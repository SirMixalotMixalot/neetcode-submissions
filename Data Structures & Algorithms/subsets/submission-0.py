class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # either add a number or dont add a number
        # when we add a number to our current set, remove from nums and then get all subsets of nums and add it
        # when we don't add, get all subsets with nums
        ans = [] # list of subsets, start with empty

        # current_sub
        # either add number to it or don't, only recurs on added bit
        def recur(nums, current):
            nonlocal ans
            if not nums:
                return ans.append(current)
            v = nums.pop()
            recur(nums[:], current + [v])
            recur(nums[:], current)
        recur(nums, [])
        return ans
                

        
        