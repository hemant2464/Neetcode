class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        n = len(height)

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                ans += bounded_height * distance

            stack.append(i)

        return ans