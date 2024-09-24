class Solution:
    def LRA(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                elem = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                max_area = max(max_area, heights[elem] * (nse - pse - 1))
            stack.append(i)

        while stack:
            nse = n  
            elem = stack.pop()
            pse = stack[-1] if stack else -1
            max_area = max(max_area, (nse - pse - 1) * heights[elem])

        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        maxarea = 0
        psum = [[None]*m for _ in range(n)]
        for j in range(m-1,-1,-1):
            s = 0 
            for i in range(n):
                s+=int(matrix[i][j])
                if matrix[i][j] == "0":
                    s = 0
                psum[i][j] = s
        for i in range(n):
            maxarea = max(maxarea, self.LRA(psum[i]))
        return maxarea