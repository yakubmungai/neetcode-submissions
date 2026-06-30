'''
#U: input is integer array 'heights', where heights[i] respresents the
    height of i-th bar.

    I may choose any two bars to form a container that will return container with max amount of water.

Input: height = [1,7,2,5,4,7,3,6]

left = 1
right = len(height) - 1
gap = right - left

Output: 36

CONSTRAINTS:

    - 2 <= height.length <= 1000
    - 0 <= height[i] <= 1000

#P: I got to take into account bar height but also distance between bars (gap) because I
    need to calculate area

    Initialize two pointers left and right

    

    Iterate through array (for loop i)
        Initialize gap variable

        compare to see which is smaller
            tmp = smaller_val * gap
        if tmp > area:
            area = temp
    return area

#I:
'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = 0

        while right > left:
            gap = abs(left - right)

            
            temp = min(heights[left], heights[right]) * gap
        
            if temp > area:
                area = temp

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area


        
        