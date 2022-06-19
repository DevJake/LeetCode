class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        return sum([(r1-r0-1)//dist for r0, r1 in zip([0] + rungs, rungs) if r1-r0 > dist])