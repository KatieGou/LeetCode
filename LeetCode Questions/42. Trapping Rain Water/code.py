# my solution, can't pass time limit :(

class Solution:
    def trap(self, height: List[int]) -> int:
        max_height=max(height)
        total_trap=0
        for i in range(max_height):
            height=self.clean_list(height)
            water=self.current_trap(height)
            if water==-1:
                return total_trap
            total_trap+=water
            height=self.change_height(height)
        return total_trap
    
    def current_trap(self, height):
        # print(height)
        if len(height)==1 or len(height)==2:
            return -1
        water=height.count(0)
        return water
    
    def change_height(self, height):
        # print('before', height)
        height = list(map(lambda x: x - 1, height))
        for i in range(len(height)):
            if height[i]<0:
                height[i]=0
        # print('after', height)
        return height
    
    def clean_list(self, height):
        while height[0]==0:
            height.pop(0)
        while height[-1]==0:
            height.pop()
        return height

      
# solution
class Solution:
    def trap(self, height: List[int]) -> int:
        total_trap=0
        left_max=[height[0]]
        right_max=[height[-1]]
        for i in range(1, len(height)):
            left_max.append(max(left_max[i-1], height[i]))
        for j in range(len(height)-2, -1, -1):
            right_max.insert(0, max(height[j], right_max[0]))
        for k in range(len(height)):
            total_trap+=min(left_max[k], right_max[k])-height[k]
        return total_trap
