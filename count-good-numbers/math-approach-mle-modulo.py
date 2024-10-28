# Remember Modulo expressions to avoid mle 

# (A * B) % m = ((A % m) * (B % m)) % m

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # even values are 0, 2, 4, 6, 8 (count: 5)
        # prime values are 2, 3, 5, 7 (count: 4)
        
        # MLE
        #return (4**(n // 2) * 5**(n // 2) * ( 1 if (n % 2) == 0 else 5)) % (10**9 + 7)

        t = n // 2
        m = 10**9 + 7
        odd = 1 if (n % 2) == 0 else 5
        # STILL MLE
        return (((4**t) % m) * ((5**t) % m) * (7)) % m
    
# Reference online:

def modular_exponentiation(x: int, n: int, M: int) -> int:
    # Base case
    if n == 0:
        return 1
    # If n is even
    elif n % 2 == 0:
        return modular_exponentiation((x * x) % M, n // 2, M)
    # If n is odd
    else:
        return (x * modular_exponentiation((x * x) % M, (n - 1) // 2, M)) % M
