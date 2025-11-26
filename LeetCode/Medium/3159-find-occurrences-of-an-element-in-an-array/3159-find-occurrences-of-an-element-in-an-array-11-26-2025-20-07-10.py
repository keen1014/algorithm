class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        li=[]
        answer=[]
        for j in enumerate(nums):
            if j[1]==x:
                li.append(j[0])
        for i in queries:
            if i<=len(li):
                answer.append(li[i-1])
            else:
                answer.append(-1)
        return answer