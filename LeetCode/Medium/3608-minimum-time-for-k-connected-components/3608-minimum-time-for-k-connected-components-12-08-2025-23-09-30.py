from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: x[2], reverse=True)
        parent=list(range(n))
        for i in range(n):
            parent[i]=i
    
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def uni(x, y):
            rootX=find(x)
            rootY=find(y)
            if rootX!=rootY:
                parent[rootX]=rootY
                return True
            return False
        
        for i in edges:
            if n<k:
                return i[2]
            if uni(i[0], i[1]):
                n-=1
                if n<k:
                    return i[2]
        return 0