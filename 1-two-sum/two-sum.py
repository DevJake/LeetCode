class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        k = dict()
        
        for i, v in enumerate(nums):
            if t - v in k:
                return i, k[t - v]
            k[v] = i