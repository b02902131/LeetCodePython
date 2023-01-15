class Solution:
    
    def canJump(self, nums: List[int]) -> bool: 
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True

    # def canJump(self, nums: List[int]) -> bool:
    #     dp = [ False for _ in range(len(nums))]
    #     dp[-1] = True
    #     for i in range(len(nums) - 1, -1, -1):
    #         if i + nums[i] >= len(nums) - 1 or dp[i + nums[i]]:
    #             dp[i] = True
    #             j = i + 1
    #             while j <= len(nums) - 1 and dp[j] == False:
    #                 dp[j] = True
    #                 j += 1 
    #     return dp[0]