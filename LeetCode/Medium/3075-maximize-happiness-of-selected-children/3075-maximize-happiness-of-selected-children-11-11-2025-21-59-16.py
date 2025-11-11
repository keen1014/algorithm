class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        answer=0
        for i in range(1,k+1):
            if 0>happiness[i-1]-i+1:
                answer+=0
            else:
                answer+=happiness[i-1]-i+1
        return answer
