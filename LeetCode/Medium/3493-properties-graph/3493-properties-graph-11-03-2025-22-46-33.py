from itertools import combinations
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        # print(properties, k)
        n=len(properties)
        an=[1 for i in range(n)]
        answer=[]
        for i in combinations(range(n), 2):
            cnt=set()
            tmp1, tmp2=i
            for j in properties[tmp1]:
                if j in properties[tmp2]:
                    cnt.add(j)
            if len(cnt)>=k:
                answer.append([tmp1, tmp2])
        print(answer)
        adj= [[] for _ in range(n)]
        for u, v in answer:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] *n
        components=0
        print(adj)

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                components +=1
                dfs(i)
        return components
        