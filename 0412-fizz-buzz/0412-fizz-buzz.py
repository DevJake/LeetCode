class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [i%3//2*'Fizz'+i%5//4*'Buzz' or str(i+1) for i in range(n)]