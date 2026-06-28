class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        U: input - increasing array of integers, output - [index1, index2] 
        (1 - indexed) and index1 < index2 and their sum = target 
        and no duplicates
        P: Two pointer solution, opposite direction because array is sorted, I will start
        pointers at opposite ends, check if index1 < index2 and calculate sum and compare to target.
        I:
        """

        l, r = 0, len(numbers) - 1
        NumSum = 0
        res = []

        while l < r:
            NumSum = numbers[l] + numbers[r]
            if NumSum < target:
                l += 1
            elif NumSum > target:
                r -= 1
            else:
                return [l + 1, r + 1] 
        