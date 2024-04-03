class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        m = {}

        if len(list(p)) != len(s.split(' ')): return False
        if len(set(p)) != len(set(s.split(' '))): return False
        
        for p, a in zip(list(p), s.split(' ')):
            if p not in m:
                m[p] = a
            
            if m[p] != a:
                return False

        return True
