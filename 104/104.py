# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode):
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return 1 + self.maxDepth(root.right)
        if root.right == None:
            return 1 + self.maxDepth(root.left)

        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))


# [3,9,20,null,null,15,7]
n = TreeNode(3)
n.left = TreeNode(9)
n.right = TreeNode(20)
n.right.left = TreeNode(15)
n.right.right = TreeNode(7)

s = Solution()
print(s.maxDepth(n))
