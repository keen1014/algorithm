from collections import deque
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans=[]
        idx=0
        for i, v in enumerate(tasks):
            v.append(i)
        tasks.sort(key=lambda x: [x[0], x[1]])
        tasks=deque(tasks)
        dq=[]
        while dq or tasks:
            while tasks and tasks[0][0]<=idx:
                task=tasks.popleft()
                heapq.heappush(dq, [task[1], task[2]])
            if dq:
                tmp=heapq.heappop(dq)
                ans.append(tmp[1])
                idx+=tmp[0]
            else:
                idx=tasks[0][0]
        return ans