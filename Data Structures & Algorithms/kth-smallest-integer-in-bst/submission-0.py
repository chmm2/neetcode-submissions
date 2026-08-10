# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def inorder(root):
            if not root:
                return

            left = inorder(root.left)
            if left is not None:
                return left
            
            self.k-=1
            if self.k==0:
                return root.val
            
            return inorder(root.right)

        return inorder(root)