class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        U: Input - array of length n, has been rotated at a pivot btn 1 and n times, and an int target to find in nums, return index
        P: Implement a binary search with two pointers l and r, calculate mid, compare to end of list and target, adjust pointers accordingly and repeat
        I: 
        '''
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid  = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
            


        