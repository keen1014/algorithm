from collections import defaultdict
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer=0
        dic=defaultdict(int)
        for i in answers:
            dic[i]+=1

        for j in set(answers):
            if j==0:
                answer+=dic[j]
                continue
            elif j==1:
                m,n=divmod(dic[j], 2)
                answer+=m*2+n*2
                continue
            m,n=divmod(dic[j], j+1)
            answer+=m*(j+1)
            if n!=0:
                answer+=j+1
        return answer
        