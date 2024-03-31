class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = ''
        carry = 0

        for i in range(max(len(a), len(b))):
            l = a[len(a)-i-1] if i < len(a) else 0
            r = b[len(b)-i-1] if i < len(b) else 0

            l, r = int(l), int(r)

            s = sum([l, r, carry])

            match s:
                case 0:
                    out += '0'
                    carry = 0
                case 1:
                    out += '1'
                    carry = 0
                case 2:
                    out += '0'
                    carry = 1
                case 3:
                    out += '1'
                    carry = 1
        if carry == 1:
            out += '1'
        
        return out[::-1]