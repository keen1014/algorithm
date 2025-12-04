class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=-1
        mi=0
        mj=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i:j]==s[j:i:-1]:
                    if max_len<(j-i):
                        max_len=(j-i)
                        mi=i
                        mj=j
        return s[mi:mj+1]