## Brute force: loop through, if num = val, list.pop(index) but each list.pop() is O(n)

## Optimal: because order doesnt matter it would be more efficient to first sort 
## in fact, it is not... 

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.sort() # ascending
        n = len(nums)
        start = None
        end = None
        for i in range(n):
            if nums[i] == val:
                start = i
                break
        if start is not None:
            for i in reversed(range(start, n)):
                if nums[i] == val:
                    end = i + 1
                    break
        if start is not None and end is not None: 
            del nums[start:end]
            print(nums, start, end)
            ## N.B. this operation is NOT in-place nums = nums[:start]+nums[end:]
            return n - (end - start)
        else:
            return n

if __name__ == '__main__':
    # run a test case
    print(1 is (1,))
    nums = [1] #[0,1,2,2,3,0,4,2]
    val = 1
    s = Solution()
    print(s.removeElement(nums, val))