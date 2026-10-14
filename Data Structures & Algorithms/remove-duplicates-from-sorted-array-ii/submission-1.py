class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write, unique = 0, 0
        # write is the end of the range that is good (nums[:write] is correct)
        # unique is the element we have to look at
        # passed is how many writes of the current number (write - 1) we allowed
        while unique < len(nums):
            if write < 2 or (nums[write - 1] != nums[unique]) or nums[unique] != nums[write - 2]:
                nums[write] = nums[unique]
                write += 1 
            unique += 1
        return write
            

        