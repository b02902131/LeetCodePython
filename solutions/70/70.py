class Solution:
    
    # Optimized method without dp, Time O(n), Space O(1)
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        prev, curr = 1, 2

        for i in range(3, n+1):
            prev, curr = curr, prev + curr

        return curr

    # DP method
    # def climbStairs(self, n: int) -> int:

    #     

    #     if n <= 2:
    #         return n

    #     dp = [0] * (n + 1)
    #     dp[1] = 1
    #     dp[2] = 2

    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
        
    #     return dp[n]