class Solution:
    def totalMoney(self, n: int) -> int:            
        return int(sum((n%7 if (i+1)*7 > n else 7) * ((1 + (n%7 if (i+1)*7 > n else 7) + 2 * i)/2) for i in range(math.ceil(n/7))))