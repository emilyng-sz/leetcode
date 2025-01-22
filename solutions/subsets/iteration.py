# Copied from online, best to understand this again.

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            print(result)
            # loop in loop, where inner loop loops over an inrementing list (result)
            # since result is initialised with [] empty list, num will always be added to result, to achieve subset of 1 element
            result += [curr + [num] for curr in result]
        return result
    

s = Solution()
b = [1,2,3]
print(s.subsets(b))