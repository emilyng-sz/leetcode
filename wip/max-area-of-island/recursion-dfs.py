from typing import List

# implements dfs recursion algo logic (without tree structure)
# Note to self: good to re-attempt this before looking

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # First define function that checks size of an island
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                # do not count 
                return 0
            grid[i][j] = 0 # this step is very important to marke node as VISITED and to not doublecount  
            area = 1 # because i,j is 1 as checked in the if else
            # for each dfs which is 1, it will look at all four directions to check if it is connected. 
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area # is the final non associative/commutative sum

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # reduce number iterations by only checking if the grid is 1 
                    max_area = max(max_area, dfs(i, j))
        return max_area