class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d, tv = {}, {}

        for n in nums:
            if n % 2 != 0:
                continue
            d[n] = d.get(n, 0) + 1
            
            if d[n] >= max(tv.keys() or [0]):
                tv[d[n]] = tv.get(d[n], []) + [n]

        return -1 if d == {} else min(tv[max(tv.keys())])
