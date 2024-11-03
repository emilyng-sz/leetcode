# This tests thinking, how to frame the question in a way where dfs consistency can be applied
# Can create a visited array to keep track e.g. visited = [[0 for _ in range(m)] for i in range(n)]
# Copied working solution 

from typing import List

class Solution:
	def solve(self, mat: List[List[str]]) -> None:
		n=len(mat)
		m=len(mat[0])

		def dfs(i,j):
			visited[i][j]=1
			dir = [[-1,0],[0,1],[1,0],[0,-1]]
			for a,b in dir:
				row = a+i
				col = b+j
				# if row col indicies are valid, and it is desired value (to continue search) and has NOT been visited
				if row>=0 and row<n and col>=0 and col<m and mat[row][col]=='O' and not visited[row][col]:
					dfs(row,col)
					
		visited = [[0 for _ in range(m)] for i in range(n)]
		
        # loop through boarder, if it accessible by boarder tiles then we do NOT want to change
		# dfs only visits if it is a 0
		for j in range(m):
			if not visited[0][j] and mat[0][j]=='O':
				dfs(0,j)
			if not visited[n-1][j] and mat[n-1][j]=='O':
				dfs(n-1,j)
				
		for i in range(n):
			if not visited[i][0] and mat[i][0]=='O':
				dfs(i,0)
			if not visited[i][m-1] and mat[i][m-1]=='O':
				dfs(i,m-1)
		
		for i in range(n):
			for j in range(m):
				# surrounded because it was not connected to the outside and hence could not be accessed
				if not visited[i][j] and mat[i][j]=='O':
					mat[i][j]='X'
		return mat