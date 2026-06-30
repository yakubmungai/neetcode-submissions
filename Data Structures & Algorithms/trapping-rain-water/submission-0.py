'''
#U: input is an array of non-negative integers 'height', where each height[i] represents
    the height of a bar, all with width 1

    we need to return maximum area of water that can be trapped between bars.

    CONSTRAINTS:
        1 <= height.length <= 1000
        0 <= height[i] <= 1000

    Input: height = [0,2,0,3,1,0,1,3,2,1]
                         w  w   w
    Output: 9
#P: 
    Strategy:

        Water can only be trapped at a bar if there is a wall taller than 
        it on both the left side AND the right side.

        The Formula: The water trapped at any index i is determined by:
        water_at_i = min(max_left_so_far, max_right_so_far) - current_height_at_i

        Refined #P (Plan)
        
        Setup: left = 0, right = len(height) - 1, left_max = 0, right_max = 0, total_water = 0.

        Loop: While left < right: 
        
        If height[left] < height[right]:
            Is height[left] >= left_max
                Update left_max.       
            Else?       
                Add left_max - height[left] to total_water.
                Move left pointer inward.
        Else (if height[right] <= height[left]):
            Is height[right] >= right_max? 
                Update right_max.

            Else? 
                Add right_max - height[right] to total_water.
                Move right pointer inward.    
#I:
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0
        
        while left < right:
            if left_max < right_max:
                # 1. Move left pointer
                left += 1
                # 2. Update left_max
                left_max = max(left_max, height[left])
                # 3. Add to total_water
                total_water += left_max - height[left]
                
            else:
                # 1. Move right pointer
                right -= 1
                # 2. Update right_max
                right_max = max(right_max, height[right])
                # 3. Add to total_water
                total_water += right_max - height[right]         
        return total_water
        