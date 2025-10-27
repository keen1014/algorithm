class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        dp=[1 for i in range(n+1)]
        dp[0]=0
        dp[1]=0
        for i in range(2, (n//2)+1):
            if dp[i]:
                for j in range(i * i, n+1, i):
                    dp[j]=0
        answer=[]
        for i in range(2,(n//2)+1):
            if dp[i] and dp[n-i]:
                answer.append([i,n-i])
        return answer