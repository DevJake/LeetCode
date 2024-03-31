import sys

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(999999)
        return list(map(int, str(int(''.join(map(str, num))) + k)))