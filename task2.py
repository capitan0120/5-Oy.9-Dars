class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        while n:
            q = n%3
            if q:
                return False
            n //= 3
            if n == 1:
                n = 0
        return True