class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer=[]
        for i in queries:
            tmp=[]
            for v, j in enumerate(nums):
                tmp.append([v,int(j[-i[1]:])])
            tmp.sort(key=lambda x: x[1])
            answer.append(tmp[i[0]-1][0])
        return answer