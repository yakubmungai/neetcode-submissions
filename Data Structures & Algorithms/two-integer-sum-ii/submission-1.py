'''
#U: input is arrays of integers SORTED in NON-DECREASING ORDER. Output is the indices
(1-INDEXED) of two numbers, [index1, index2], such that they add up to a given target 
number 'target' and INDEX1 < INDEX2. index1 and index2 CANNOT be equal.

Note: There will be exactly ONE valid solution, and solution Must use O(1) additional 
space.

CONSTRAINTS:
    2 <= numbers.length <= 1000
    -1000 <= numbers[i] <= 1000
    -1000 <= target <= 1000
    
Input: numbers = [1,2,3,5,10] target = 8

3 + 5 = 8

8 - 5 = 3

Output: [3,4]

#P:
Strategy:
    initialize two pointers, left and right.

    while right > left:
        if numbers[left] + numbers[right] == target:
            return [left, right]
        if numbers[left] + numbers[right] > target:
            move right pointer backwards
        if numbers[left] + numbers[right] < target:
            move left pointer forwards









#I:
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)

        while right > left:
            if numbers[left - 1] + numbers[right - 1] == target:
                return [left, right]
            if numbers[left - 1] + numbers[right - 1] > target:
                right -= 1
            if numbers[left - 1] + numbers[right - 1] < target:
                left += 1
    

        

        