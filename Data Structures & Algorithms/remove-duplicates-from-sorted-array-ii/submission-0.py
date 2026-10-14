class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        passed = 0
        write, unique = 0, 0
        # write is the end of the range that is good (nums[:write] is correct)
        # unique is the element we have to look at
        # passed is how many writes of the current number (write - 1) we allowed
        while unique < len(nums):
            if write == 0 or (nums[write - 1] != nums[unique]):
                nums[write] = nums[unique]
                passed = 1 # we let a new one pass
                write += 1 
            elif nums[write - 1] == nums[unique] and passed < 2:
                nums[write] = nums[unique]
                passed += 1 # update how much we let passed
                write += 1
            unique += 1
        return write
            

        