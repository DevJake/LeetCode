class Solution:
    def is_arithmetic(self, nums: List[int]) -> bool:
        s = sorted(nums)
        
        for i in range(1, len(s)):
            if s[i] - s[i-1] != s[1] - s[0]:
                return False

        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [self.is_arithmetic(nums[l:r+1]) for l, r in zip(l, r)]