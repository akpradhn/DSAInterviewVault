class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        best = 0

        for right in range(len(heights) + 1):
            current_height = 0 if right == len(heights) else heights[right]

            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, height * (right - left - 1))

            stack.append(right)

        return best
