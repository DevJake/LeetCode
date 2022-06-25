class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d = {0: 0}
        
        res, sum = 0, 0
        
        for i in range(len(nums)):
            sum += nums[i]
            
            if (sum-target) in d:
                res = max(res, d[sum-target] + 1)
                
            d[sum] = res
            
        return res