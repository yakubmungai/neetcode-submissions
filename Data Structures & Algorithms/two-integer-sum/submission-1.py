'''
U: input is an array of integers nums and a target, output is indices i and j
where nums[i] + nums[j] == target and i != j

P: I'll convert the nums list to a set, then I'll run a for loop through nums,
and check target - num, if that's in the set I stop and return indices

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