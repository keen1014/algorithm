from collections import deque
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles=deque(piles)
        answer=0
        n=0
        while piles:
            if n==0:
                piles.pop()
            elif n==1:
                answer+=piles.pop()
            else:
                piles.popleft()
            n+=1
            if n==3:
                n=0
        return answer