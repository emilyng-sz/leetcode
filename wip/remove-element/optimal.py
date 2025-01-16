# Instead of sorting, realise that only the first k elements of the list matters. i.e. the first k can be REPLACED

class Solution():
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i] # replaces index-th value with non-val value.
                index += 1
        return index 
    
## Time complexity: O(n)
## Space complecity: O(1)