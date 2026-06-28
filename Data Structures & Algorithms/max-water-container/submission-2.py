class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        #U: Input is array height, I am trying to find max area between two vertical height n, and x axis
        #P: Two pointer approach (opposite directions), calculate area, store it,move shorter line pointer 
        #I:

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            max_area = max(max_area, (r - l) * min(heights[r],heights[l]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r-= 1
        return max_area
