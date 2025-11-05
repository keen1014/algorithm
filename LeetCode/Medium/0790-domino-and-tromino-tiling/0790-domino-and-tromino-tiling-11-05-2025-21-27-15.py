class Solution:
    def numTilings(self, n: int) -> int:
        dp=[0]*(1000+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        dp[3]=5
        for i in range(4,n+1):
            dp[i]=dp[i-1]*2 + dp[i-3]
        return dp[n]%1000000007