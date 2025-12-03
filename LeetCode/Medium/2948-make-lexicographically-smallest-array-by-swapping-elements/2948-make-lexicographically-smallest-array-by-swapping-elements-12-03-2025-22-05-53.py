from collections import defaultdict
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ans=[0]*len(nums)
        li=[]
        dic=defaultdict(set)
        for i, v in enumerate(nums):
            li.append((v, i))
        li.sort()
        idx=0
        dic[idx].add(li[0])
        for i in range(len(li)-1):
            dic[idx].add(li[i])
            if abs(li[i][0]-li[i+1][0])<=limit:
                dic[idx].add(li[i+1])
            else:
                idx+=1
                dic[idx].add(li[i+1])
        for key in dic:
            group=dic[key]
            value=sorted([item[0] for item in group])
            index=sorted([item[1] for item in group])
            for z in range(len(value)):
                ans[index[z]]=value[z]
        return ans