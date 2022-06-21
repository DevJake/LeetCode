class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0 # maximum jump from current index
        for i, n in enumerate(nums):
            if i > k: # If the index we're at exceeds k, then we're at an index it is not possible for us to reach so far... we've hit a deadend
                return False
            
            k = max(i+n, k) # jump as far as we can from the current index. If this index doesn't get us closer than a previous attempt (stored by k), then revert to k
            
        return True # No deadends... we've made it!