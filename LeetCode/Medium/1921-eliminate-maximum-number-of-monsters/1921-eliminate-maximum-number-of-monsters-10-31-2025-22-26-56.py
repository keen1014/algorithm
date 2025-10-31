class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        answer=0
        qu=[]
        for i in range(len(dist)):
            qu.append(dist[i]/speed[i])
        qu.sort()
        for j in range(len(qu)):
            if qu[j]<=j:
                return answer
            answer+=1
        return answer