# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        left = []
        right = []
        self.preorder(root, left)
        self.preorder(subRoot, right)

        for i in range(len(left) - len(right) + 1):
            if left[i:i+len(right)] == right:
                return True
        return False

    
    def preorder(self, root, arr):
        if root is None:
            arr.append("null")
            return 
            
        
        arr.append(root.val)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
