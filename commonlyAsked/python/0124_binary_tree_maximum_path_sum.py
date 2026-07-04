class Solution:
    def maxPathSum(self, root):
        self.best = float("-inf")
        self.maxGain(root)
        return self.best

    def maxGain(self, node):
        if not node:
            return 0

        left_gain = max(self.maxGain(node.left), 0)
        right_gain = max(self.maxGain(node.right), 0)

        self.best = max(self.best, node.val + left_gain + right_gain)

        return node.val + max(left_gain, right_gain)
