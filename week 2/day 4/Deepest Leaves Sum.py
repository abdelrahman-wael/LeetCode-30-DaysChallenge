# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    
    def findDepth(self,node):
        leftBranch = 0
        rightBranch = 0
        if node == None:
            return 0
        if node.right:
            rightBranch = 1 + self.findDepth(node.right)
        if node.left:
            leftBranch = 1 + self.findDepth(node.left)
        
        return max(rightBranch,leftBranch)
    
    def findSum(self,node,depth):
        sum1=0
        sum2=0
        if depth == 0:
            return node.val
        if node.right != None:
            sum1 = self.findSum(node.right,depth-1)
        if node.left != None:
            sum2 = self.findSum(node.left,depth-1)
        return sum1+sum2
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = self.findDepth(root)
        return self.findSum(root,depth)
        
