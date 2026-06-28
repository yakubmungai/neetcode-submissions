class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through list
            # At each index, add to other indexes and compare to target
                # if sum equals target, store the indexes, smallest first
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)


        