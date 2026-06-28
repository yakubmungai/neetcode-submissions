'''
U: 
- Input: A list of integers (nums) and an integer (target).
- Output: A list containing two indices [i, j] where nums[i] + nums[j] == target.
- Constraints: i != j (cannot use the exact same element twice). The indices should be sorted.

P:
- Create an empty dictionary (previous_numbers) to map seen numbers to their indices.
- Loop through nums tracking both the current index and value.
- For each number, calculate its complement (target - num).
- Check if that complement is already in our dictionary:
    - If it is: We found our pair! Return the sorted indices of the current number and the complement.
    - If it isn't: Store the current number and its index in the dictionary for future checks.
I:
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_numbers = {}
        res = []

        for index, num in enumerate(nums):
            complement = target - num
    
            if complement in previous_numbers:
                return sorted([index, previous_numbers[complement]])
    
            previous_numbers[num] = index