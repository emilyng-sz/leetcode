# Copied from online, best to understand this again.

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            print(start, path)
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result
    
s = Solution()
b = [1,2,3]
print(s.subsets(b))