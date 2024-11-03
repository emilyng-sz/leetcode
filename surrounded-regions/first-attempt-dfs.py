# Non-working solution. Wrong answer, 25/58 TC passed

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if cell is 0, if it is NOT on the edge, and if it can connect vertically/horizontally w X then it should be replaced
        # loop through board, if '0' save it to an index 
        # REGION. Need to DETECT region. and if any part of the region can connect to a X then should replace it with X 
        ROW, COL = len(board), len(board[0])
        ### IN FUTURE, let row be i, col be j 
        def is_edge(i,j):
            return i == COL-1 or j == ROW-1
        def connected_to_X(i,j):
            if not is_edge(i,j):
                return board[j-1][i] == 'X' or board[j][i-1] == 'X' or board[j+1][i] == 'X' or board[j][i+1] == 'X'

        def dfs(i,j): # note i, j will always initially be valid
            # to find region
            if i >= COL or j >= ROW: # when finding region
                return True # ends because region is found 
            if board[j][i] == 'O' and is_edge(i,j):
                print("False is returned")
                return False # stop because region is found but sticks to edge
            if board[j][i] == 'O':
                stack.append((j,i))
                if dfs(i+1, j):
                    dfs(i, j+1)
                    return True
                else:
                    return False
            # if grid == 'X': # then ntg is done
        print("Start solve")

        ## IN FUTURE, do not try to optimise it here. This causes my third board b to fail.
        for j in range(1, ROW-1):
            for i in range(1, COL-1): # to prevent starting from edge
                stack = [] # just to store the region for capturing (set to X)
                if board[j][i] == "O":
                    print(j,i)
                    if dfs(i, j): # is True and it is a valid region
                        print(stack)
                        for index in stack:
                            i,j = index[1], index[0]
                            print(i,j)
                            if not is_edge(i,j) and connected_to_X(i,j):
                                # if any 1 of the region is connected
                                while stack:
                                    j, i = stack.pop()
                                    board[j][i] = 'X' # capture region
                                break # out of checking because no more index in stack
                            
                # would be good to implement a way to bypass non-captured regions without doing dfs again
        
      

s = Solution()
b = [["X","X","X","X"],
     ["X","O","O","X"],
     ["X","X","O","X"],
     ["X","O","X","X"]]
b = [["O","O","O"],
     ["O","O","O"],
     ["O","O","O"]]

b = [["X","O","X"],
     ["X","O","X"],
     ["X","O","X"]]
s.solve(b)
print(b)