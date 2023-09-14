# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,lowerB,upperB):
            if not (node.val > lowerB and node.val < upperB):
                return False
            
            if node.left != None:
                if(dfs(node.left,lowerB,node.val) == False):
                    return False
            if node.right != None:
                if(dfs(node.right,node.val,upperB) == False):
                    return False
            
            return True
        
        return dfs(root,-inf,inf)