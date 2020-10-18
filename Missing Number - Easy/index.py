class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        currentSum = sum(nums)
        n = len(nums)
        requiredSum = n * (n + 1)//2
        return requiredSum-currentSum