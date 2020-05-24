class Solution:
    def __init__(self):
        self.n=0
        self.k=0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root:
            self.kthSmallest(root.left,k)
            self.n+=1
            if self.n==k:
                print(root.val)
                return root.val
            self.kthSmallest(root.right,k)
