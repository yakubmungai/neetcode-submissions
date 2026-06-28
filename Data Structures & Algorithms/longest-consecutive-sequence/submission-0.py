'''

Refined #U (Understand):

    Input: An unsorted array of integers nums.
    Output: The length of the longest sequence of consecutive integers.
    Constraints: Must run in $O(n)$ time.Sequence elements don't need 
    to be adjacent in the original array.
    Example: [1, 5, 3, 4, 9] -> Sequence is [1] (len 1) and [3, 4, 5] (len 3). Max length is 3.

Refined #P (Plan)
Strategy: Use a Hash Set for $O(1)$ lookups to find sequence starts. 
Steps: 
    Convert the nums list into a set called numSet. (This removes duplicates and allows fast searching).
    Iterate through each num in the numSet. The "Start of Sequence" 
        Check: Only start counting if num - 1 is not in the set. This ensures we only begin counting from the smallest number 
        in any potential sequence, preventing redundant work. 

        The "While" Loop: Once a start is found, keep checking for num + 1, num + 2, etc., until the sequence breaks.
        Track Max: Update longest with the length found. 
        
        Why this is O(n): It looks like $O(n^2)$ because of the while loop inside the for loop, 
        but it is actually $O(n)$.Because we only start the while loop when num - 1 is not in the set, 
        each number in the array is visited by the while loop at most once. Every number is either a "start" 
        of a sequence or it is eventually part of a sequence counted by a "start" number.
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        