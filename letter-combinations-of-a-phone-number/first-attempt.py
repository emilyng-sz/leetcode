# Working solution 
## Can consider implementing backtracking approach

from collections import deque
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        characters = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6": "mno", "7":"pqrs", 8: "tuv", "9":"wxyz"}
        ls = []

        if not digits:
            return ls

        else:
            ls = deque(list(chara for chara in characters[digits[0]]))
            # e.g. a, b, c

            for digit in digits[1:]:
                for _ in range(len(ls)):
                    letters = ls.popleft()
                    for chara in characters[digit]: #e.g. d , e , f
                        ls.append(letters+chara)
            return list(ls) ## MUST REMEMBER TO CONVERT DEQUE TO LIST AT THE END

if __name__ == '__main__':
    # run a test case
    s = Solution()
    print(s.letterCombinations("23"))