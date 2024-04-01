class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s = sorted(arr)
        for i in range(1, len(arr)):
            if s[i] - s[i-1] != s[1] - s[0]:
                return False

        return True