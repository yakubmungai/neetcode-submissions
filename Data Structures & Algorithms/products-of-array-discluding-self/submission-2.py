'''
Refined #U (Understand)Your current notes are good, 
but let's add the constraints to ensure you don't miss edge cases.

Input: Integer array nums.Output: Integer array output where output[i] = product of all elements 
except nums[i].Constraints/Rules: * No division allowed.$O(n)$ time complexity required.
Result fits in a 32-bit integer.Handle edge cases: Zeros (if array has one 0, only that index gets
 a product; if array has two or more 0s, all outputs are 0).
 
 Refined #P (Plan)Your plan needs to capture the "re-use" logic to prove to an interviewer you understand 
 space complexity.
 
 Goal: Calculate prefix_product[i] * suffix_product[i] for every index without using division.
 
 Strategy: Two-pass traversal.
 
 Prefix Pass (Forward): Iterate left-to-right. Use a running variable prefix to calculate the product of everything
  before the current index and store it in output[i].
  
 Suffix Pass (Backward): Iterate right-to-left. Use a running variable suffix to calculate the product of everything 
 after the current index, and multiply it directly into output[i] (which currently holds the prefix product).
 
 Space Optimization: By multiplying the suffix into the output array directly, we achieve $O(1)$ extra space (excluding the output array).
'''
'''
prefix = 6
nums = [1, 2, 3, 4]
output = [1, 1, 2, 6]

suffix = 24
nums = [1, 2, 3, 4]
output = [24, 12, 8, 6]


res = [24, 12, 8, 6]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # identify prefix variable
        prefix = 1

        # iterate through list to store prefixes (left products)
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        # now i need to iterate through same array and multiply the suffixes (right products)
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]


        return output
            
            

            


        
            
        
        