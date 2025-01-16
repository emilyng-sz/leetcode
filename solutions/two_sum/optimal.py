from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Finds two numbers in nums that add up to target.

        :param nums: List of integers
        :param target: Target sum
        :return: Indices of the two numbers
        
        '''
        dct = {}
        for i in range(len(nums)):
            if target - nums[i] in dct:
                return [i,dct[target - nums[i]]]
            dct[nums[i]] = i
            
        return []