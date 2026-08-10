class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0]*n
        right = [0]*n
        stack1 = []

        for i in range(n):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                stack1.pop()

            if not stack1:
                left[i] = 0
            else:
                left[i] = stack1[-1] + 1
            
            stack1.append(i)
        stack1 = []
        for i in range(n-1,-1,-1):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                stack1.pop()

            if not stack1:
                right[i] = n-1
            else:
                right[i] = stack1[-1] - 1
            
            stack1.append(i)
        f = 0
        for i in range(n):
            temp = (right[i]-left[i]+1) * heights[i]
            f = max(f,temp)
        return f
            

        
