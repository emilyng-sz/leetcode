# Working solution but TLE

## mainly because each string concatenation takes O(n), this may be O(n^3) time
## solution requires a mathematical approach instead of deciphering the entier nth row from the top.

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        string = "0"
        def buildKthRow(n, string):
            if n == 1:
                return string
            else:
                new = ""
                for chara in string:
                    if chara == "0":
                        new += "01"
                    else:
                        new += "10"
                return buildKthRow(n-1, new)
        
        return int(buildKthRow(n, string)[k-1])
