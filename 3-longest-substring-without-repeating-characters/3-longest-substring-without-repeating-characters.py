class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = right = 0
        longest = 0
        
        for right, c in enumerate(s):
            if c not in s[left:right]:
                longest = max(longest, right+1-left)
            else:
                if d[c] < left:
                    longest = max(longest, right+1-left)
                else:
                    left = d[c] + 1
        
            d[c] = right
        
        return longest
            
        