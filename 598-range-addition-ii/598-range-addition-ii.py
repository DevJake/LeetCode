import numpy as np

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        i, j = m, n
        
        for (x, y) in ops:
            i, j = min(x, i), min(y, j)
            
        return i * j
    
    
    
        
        