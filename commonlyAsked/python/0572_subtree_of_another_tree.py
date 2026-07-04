class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.val == right.val
            and self.isSameTree(left.left, right.left)
            and self.isSameTree(left.right, right.right)
        )
