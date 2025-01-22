# A very unelegant recursion. 
# Takes very long time because I check if there are non duplicates before adding
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        given a nums, for each 
        '''
        lst = []
        def helper(nums):
            if not nums:
                return lst
            else:
                if nums not in lst:
                    lst.append(nums)
                for i in range(len(nums)):
                    helper(nums[:i]+nums[i+1:])
        helper(nums)
        lst.append([])
        return lst
    '''
        # [1,2,3] -> [1], [2], [3] -> call([1)
        # # recursion call [1,2,3], [2,3], [3], 
        # base case , return [] if empty 
        # else: for i in nums: [1,2], return[1], [2,3]
        def permutes_with_first(numbers, to_update):
            # eg 3 [1,2,3]: 0,1,2
            for i in range(1, len(numbers)+1):
                to_update.append(numbers[:i])

        for i in range(nums):
            permutes_with_first(nums[i:], lst)
            

            lst.append(nums)
        lst = []
        def helper(nums):
            if not nums:
                # if empty
                lst.append([])
                print("base case")
                return lst
            else:
                lst.append(nums) 
                lst.append(helper[0])
                lst.append(helper(nums[1:]))

        return helper(nums)
    '''
s = Solution()
b = [1,2,3]
print(s.subsets(b))