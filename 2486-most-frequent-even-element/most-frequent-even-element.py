class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d, tv = {}, {}

        for n in nums:
            if n % 2 != 0:
                continue
            d[n] = d.get(n, 0) + 1
            
            if d[n] >= max(tv.keys() or [0]):
                if d[n] not in tv:
                    tv[d[n]] = []
                tv[d[n]].append(n)

        return -1 if d == {} else min(tv[max(tv.keys())])
