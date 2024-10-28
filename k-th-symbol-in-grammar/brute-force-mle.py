## Memory Lmit Exceeded

# Understand how to do this using a mathematical and recursive approach.

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        string = "0"
        ind = 1
        while ind <= k:
            string = "".join("01" if char == "0" else "10" for char in string)
        return string[-1]
    