class Solution:
    def isValidBST(self, root):
        return self.isValid(root, None, None)

    def isValid(self, node, lower, upper):
        if not node:
            return True
        if lower is not None and node.val <= lower:
            return False
        if upper is not None and node.val >= upper:
            return False

        return self.isValid(node.left, lower, node.val) and self.isValid(node.right, node.val, upper)
