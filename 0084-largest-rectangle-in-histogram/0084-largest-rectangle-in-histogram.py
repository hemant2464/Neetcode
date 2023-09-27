class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxval = [], 0
        heights.append(0)

        for index in range(len(heights)):
            while stack and heights[stack[-1]] > heights[index]:
                cur = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                maxval = max(maxval, (index - left - 1) * heights[cur])
            stack.append(index)

        return maxval