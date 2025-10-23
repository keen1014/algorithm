class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        n=int(n**0.5)
        return n