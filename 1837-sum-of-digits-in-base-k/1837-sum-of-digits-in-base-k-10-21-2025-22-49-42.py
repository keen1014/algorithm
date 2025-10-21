class Solution:
    def sumBase(self, n: int, k: int) -> int:
        li=[]
        while n:
            n, divide=divmod(n,k)
            li.append(divide)
        return sum(li)