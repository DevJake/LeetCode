class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = {
            0: ('0', 0),
            1: ('1', 0),
            2: ('0', 1),
            3: ('1', 1)
        }

        o, c = '', 0

        for i in range(max(len(a), len(b))):
            s = sum([int(a[len(a)-i-1] if i < len(a) else 0), int(b[len(b)-i-1] if i < len(b) else 0), c])

            g, f = m[s]
            o += g
            c = f

        if c == 1:
            o += '1'
        
        return o[::-1]