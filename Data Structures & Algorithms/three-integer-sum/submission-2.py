'''
Refined #U (Understand)
Goal: Find all unique triplets [nums[i], nums[j], nums[k]] such that 
      their sum is 0.

Key Constraints:

    - Distinct Indices: i != j, i != k, j != k.

    - No Duplicate Triplets: [-1, 0, 1] and [0, 1, -1] are the same set; 
      you must output only one.

    - The "Trick": Since the array is sorted, for a fixed index i, we need to find two other 
      numbers (j and k) that sum to -nums[i]. This turns the problem into a "Two Sum" problem 
      on a sorted array!

    - -nums[k] = nums[i] + nums[j]

Refined #P (Plan)
Sort the array: nums.sort() — this is mandatory for the Two Pointers pattern.

Iterate through the array: Use a loop for index i (from 0 to len(nums) - 2).

Optimization: If i > 0 and nums[i] == nums[i-1], skip it to avoid duplicate triplets 
              starting with the same value.

Two Pointers: Set left = i + 1 and right = len(nums) - 1.

Calculate sum = nums[i] + nums[left] + nums[right].

If sum < 0: We need a larger number, so left += 1.

If sum > 0: We need a smaller number, so right -= 1.

If sum == 0:

Add [nums[i], nums[left], nums[right]] to your results.

Skip duplicates: While left < right and nums[left] == nums[left + 1], left += 1.

Move pointers: left += 1 and right -= 1.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort() # Fix 1: Sort in-place
        
        for i in range(0, len(nums) - 2):
            if (i > 0) and (nums[i] == nums[i - 1]):
                continue
                
            left = i + 1 
            right = len(nums) - 1
            
            # Fix 2: You need the while loop to hunt for the sum
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # Fix 3: Append the actual list, not the sum
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return triplets

