class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        for i, l in enumerate(s):
            if l not in mapping and t[i] not in mapping.values():
                mapping[l] = t[i]
            if mapping.get(l, '') != t[i]:
                return False
        return True