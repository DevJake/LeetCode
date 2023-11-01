# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    c = 1
    deepest = c
    def dfs(self, nodes, n):
        if n and n not in nodes:
            nodes.append(n)
            if n.left:
                self.c += 1
                self.dfs(nodes, n.left)
                if self.c > self.deepest:
                    self.deepest = self.c
                self.c -= 1
            if n.right:
                self.c += 1
                self.dfs(nodes, n.right)
                if self.c > self.deepest:
                    self.deepest = self.c
                self.c -= 1
    
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        nodes = []
        self.dfs(nodes, root)
        return self.deepest
