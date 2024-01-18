#                                                    Leetcode 70. Climbing Stairs
#--------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# When n=3, 
#   dp[3] = dp[2] + dp[1]
#   dp[3] = 1 + 1  =  2

# When n = 4,
#   dp[4] = dp[3] + dp[2]
#   dp[5] = 2 + 1  =  3

# When n = 5,
#   dp[5] = dp[4] + dp[3]
#   dp[5] = 3 + 2  =  5
