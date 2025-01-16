# Working Solution but TLE because Time: O(2^m+n), Space O(m+n)
# https://leetcode.com/problems/unique-paths/description/ 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: 
            return 1
        if m < 1 or n < 1:
            return 0
        else:
            return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

## Need to implement memoisation / dynamic programming