class Solution:
    def maxArea(self, height: List[int]) -> int:
        def container(h1, h2, idx1, idx2):
            assert (idx2>idx1)
            return min(h1, h2)*(idx2-idx1)
        
        number=len(height)
        i, j=0,number-1
        max_contain=0
        while (i<j):
            contain=container(height[i], height[j], i, j)
            if contain>max_contain:
                max_contain=contain
            
            # move the shorter one (moving the larger one cannot improve)
            # embedded for loops are wasting time
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return max_contain
