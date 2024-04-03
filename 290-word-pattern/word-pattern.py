class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        seen = set()

        if len(list(pattern)) != len(s.split(' ')):
            return False
        
        for p, a in zip(list(pattern), s.split(' ')):
            if p not in m:
                if a in seen:
                    return False
                m[p] = a
                seen.add(a)
            
            if m[p] != a:
                return False

        return True
