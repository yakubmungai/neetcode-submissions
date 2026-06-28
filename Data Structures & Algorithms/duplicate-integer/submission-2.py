'''
U: input is integer array, output is Boolean if any value appears more than once in the array.

P: I'll convert the array into a dictionary where key is number, and value is count of how many times it appears. 
I plan to use Counter from collections. Then I'll just check dictionary for items with value more than 1 and 
return True else return False.

I:
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counter_nums = Counter(nums)

        for key, value in counter_nums.items():
            if value > 1:
                return True
        return False
