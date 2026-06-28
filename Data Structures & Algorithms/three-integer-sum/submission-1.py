class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #U: For each element in array, I need to add two other elements such that the triplet contains no duplicate, and sum of triplets is equal to 0, and no duplicate triplets.
        #P: Brute force approach, nested for loops to iterate through all elements, I will use if statements to ensure elements not equal, and then calculate triplet sum to check if 0, if yes then append it to res array
        #I:
        res = []
        tripletSum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j,len(nums)):
                    if i != j and i != k and j != k:
                        tripletSum = nums[i] + nums[j] + nums[k]
                        if tripletSum == 0:
                            triplet = sorted([nums[i],nums[j],nums[k]])
                            if triplet not in res:
                                res.append(triplet)
        return res