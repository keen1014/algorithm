from collections import defaultdict
from collections import deque
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        answer=0
        max_def=0
        properties.sort(key=lambda x: (-x[0], x[1]))
        print(properties)
        for i in properties:
            if i[1]<max_def:
                answer+=1
            if max_def<i[1]:
                max_def=i[1]
            
        return answer
        # dic=defaultdict(list)
        # for i in range(len(properties)):
        #     dic[properties[i][0]].append(properties[i][1])
        # print(dic.keys())
        # dq=deque(dic.keys())

        # for j in range(len(properties)):
        #     loop=True
        #     if dq and dq[0]==properties[j][0]:
        #         dq.popleft()
        #     for k in dq:
        #         if dic[k]!=[] and k>properties[j][0]:
        #             if max(dic[k])>properties[j][1]:
        #                 answer+=1
        #                 break
        # return answer