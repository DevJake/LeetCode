class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = o = 0
        
        for r, c in enumerate(s):
            if c not in s[l:r] or d[c] < l:
                o = max(o, r+1-l)
            else:
                l = d[c] + 1
        
            d[c] = r
        
        return o
            
        