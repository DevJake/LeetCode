import sys

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(999999)
        return [int(i) for i in str(int(''.join(str(n) for n in num)) + k)]