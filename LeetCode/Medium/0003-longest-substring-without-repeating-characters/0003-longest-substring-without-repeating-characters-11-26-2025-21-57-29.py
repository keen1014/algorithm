from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer=0
        now=0
        li=deque([])
        while len(s)!=now:
            if li!=deque([]) and s[now] in li:
                while li[0]!=s[now]:
                    li.popleft()
                li.popleft()
            if s[now] not in li:
                li.append(s[now])
                if len(li)>answer:
                    answer=len(li)
            now+=1
        return answer
