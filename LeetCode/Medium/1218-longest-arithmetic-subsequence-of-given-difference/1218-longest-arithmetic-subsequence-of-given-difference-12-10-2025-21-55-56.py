class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}
        max_len=0
        for i in arr:
            before=i-difference
            if before in dp:
                dp[i]=dp[before]+1
            else:
                dp[i]=1
            max_len=max(max_len, dp[i])
        return max_len
        # dic={}
        # ans=0
        
        # for i, v in enumerate(arr):
        #     if v not in dic:
        #         dic[v]=[i]
        #     else:
        #         dic[v].append(i)
        # dickey=list(dic.keys())
        
        # if difference<0:
        #     dickey.sort(reverse=True)
        # else:
        #     dickey.sort()
        
        # for j in dickey:
        #     dic[j].sort()

        # for j in dickey:
        #     maxlen=1
        #     now=min(dic[j])
        #     diff=j+difference
        #     while diff in dickey:
        #         for z in dic[diff]:
        #             if now<z:
        #                 now=z
        #                 break
        #         else:
        #             break
        #         maxlen+=1
        #         diff+=difference
        #     if ans<maxlen:
        #         ans=maxlen
        # return ans
        
        # =================================================
        
        # answer=0
        # arr=list(set(arr))
        # if difference<0:
        #     arr.sort()
        # else:
        #     arr.sort(reverse=True)
        # dic={}
        # for i in arr:
        #     diff=i+difference
        #     if diff not in dic:
        #         dic[i]=1
        #     else:
        #         dic[i]=dic[diff]+1
        # return max(dic.values())
        