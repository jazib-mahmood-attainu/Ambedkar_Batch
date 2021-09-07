class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water_trapped = 0
        
        for idx,h in enumerate(height):
            
            max_ht_r = float("-inf")
            for i in range(idx+1,n):
                if height[i]>max_ht_r:
                    max_ht_r = height[i]
                    
            max_ht_l = float("-inf")
            for i in range(0,idx):
                if height[i]>max_ht_l:
                    max_ht_l = height[i]
            
            water_trapped = min(max_ht_r,max_ht_l) - height[idx]

            if water_trapped>0:
                total_water_trapped += water_trapped
            
        return total_water_trapped