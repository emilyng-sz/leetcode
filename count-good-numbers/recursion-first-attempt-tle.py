# 66 / 156 test case passed

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # even values are 0, 2, 4, 6, 8 (count: 5)
        # prime values are 2, 3, 5, 7 (count: 4)
        
        # use permuations??

        def helper(n, EVEN):
            if n == 1:
                return 5
            elif EVEN:
                return 5 * helper(n-1, False)
            else:
                return 4 * helper(n-1, True)

        return (helper(n, False)) % (10**9 + 7)

        