class Solution:
    def f_prime(self, x: int) -> float:
        return 2*x

    def f(self, x: float, t: int) -> float:
        return x*x - t

    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        x0 = x/2

        epsilon, tolerance = 1e-6, 0.1

        while True:
            y = self.f(x0, x)
            y_p = self.f_prime(x0)

            if abs(y_p) < epsilon:
                break

            x1 = x0 - y / y_p

            if abs(x1 - x0) <= tolerance:
                return int(x1)
            
            x0 = x1

        return int(x0)