class Solution:
    def mySqrt(self, x: int) -> int:        
        x0 = x + 1

        while x0*x0 > x:
            x0 = int(x0 - (x0*x0-x)/(2*x0))

        return x0