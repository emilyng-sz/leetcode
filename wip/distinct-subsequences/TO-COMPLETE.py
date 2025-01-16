# HARD question, should be testing recursion

# https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # recursion should be implemented. 
        # potentially use hashmap to improve time. 
        
        # for every "r", "ra", "rab"... of t:
        #   find all occurance of "X" in s
        #   for each occurance:
        #       find all occurance of remaining "a", "ab" and repeat, without double countingg 
        ## Abbove approach NOT GOOD
        ## Take hints from example and use greedy(?) approach instead

        if len(s) < len(t):
            return 0
        
        if s == t:
            return 1
        # null case? 
        elif s[0] == t[0]:
            return self.numDistinct(s[1:], t[1:])
            
        elif s[0] != t[0]:
            return self.numDistinct(s[1:], t[1:])