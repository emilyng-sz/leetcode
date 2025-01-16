class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        https://leetcode.com/problems/two-sum/
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                #counter += 1
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

## Note to self
# Time complexity: O(n^2)
# Best to assign n = len(nums)
# Return something if no solution is found
# Note that an alternate way is to iterate up to len(nums) - 1, but my second loop will avoid redundancies

if __name__ == '__main__':
    nums = [2, 7, 11, 15, 5]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))