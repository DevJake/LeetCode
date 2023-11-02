class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (max(nums)-1) * (max([j for i, j in enumerate(nums) if i != nums.index(max(nums))])-1)