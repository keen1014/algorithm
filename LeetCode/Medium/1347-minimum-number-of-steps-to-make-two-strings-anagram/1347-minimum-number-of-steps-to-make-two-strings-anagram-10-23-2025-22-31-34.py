from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic1=defaultdict(int)
        dic2=defaultdict(int)
        for i in range(len(s)):
            dic1[s[i]]+=1
            dic2[t[i]]+=1
        print(dic1.values())
        for j in dic1.keys():
            if j in dic2.keys():
                if dic2[j]<dic1[j]:
                    dic1[j]-=dic2[j]
                else:
                    dic1[j]=0
        return sum(dic1.values())