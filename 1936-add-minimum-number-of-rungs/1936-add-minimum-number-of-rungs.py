class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        space = (rungs[0]-1)//dist
        for r0, r1 in zip(rungs, rungs[1:]):
            
            print(r0, r1)
            
            if r1-r0 > dist:
                space += (r1-r0-1)//dist
                
        return space
        