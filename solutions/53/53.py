class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndHere = maxSoFar = nums[0]
        for x in nums[1:]:
            maxEndHere = max(x, x + maxEndHere)
            maxSoFar = max(maxSoFar, maxEndHere)
        return maxSoFar