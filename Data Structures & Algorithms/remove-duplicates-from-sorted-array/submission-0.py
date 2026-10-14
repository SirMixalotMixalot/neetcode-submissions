class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # in place huh, 
        # [1, 2, 3, 3, 4]
        #              ^ [1, 2, 3, 4] good
        # [1, 2, 3, 4, 1]
        write, unique = 0, 0
        # write is the num of written items (nums[:write] is good)
        # unique is the next value to check
        while unique < len(nums):
            if write == 0 or nums[unique] != nums[write - 1]:
                nums[write] = nums[unique]
                write += 1
            unique += 1

              
        return write
            
        