class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v = {'a', 'e', 'i', 'o', 'u'}

        ans, lc = 0, -1
        lv = {j: -1 for j in v}

        for i, x in enumerate(word):
            if x not in v:
                lc = i
            else:
                lv[x] = i
                ans += max(min(lv.values())-lc, 0)
            print(f'{lc=}, {lv=}, {ans=}')

        return ans