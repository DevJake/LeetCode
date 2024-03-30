class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most_k(nums, k) - self.at_most_k(nums, k-1)
    
    def at_most_k(self, nums: List[int], k: int) -> int:
        unique = {}

        left, right, ans = 0, 0, 0

        while right < len(nums):
            unique[nums[right]] = unique.get(nums[right], 0) + 1
            
            while len(unique) > k:
                unique[nums[left]] = unique.get(nums[left]) - 1

                if unique[nums[left]] == 0:
                    del unique[nums[left]]

                left += 1
            
            ans += right - left + 1
            right += 1
            
        return ans


