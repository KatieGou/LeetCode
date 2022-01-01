class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=heights+[0]
        stack=list()
        maxA=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                height=heights[stack.pop()]
                if stack:
                    curA=height*(i-stack[-1]-1)
                else:
                    curA=height*i
                maxA=max(maxA, curA)
            stack.append(i)
        return maxA
