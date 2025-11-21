class Solution:
    def numSquares(self, n: int) -> int:
        li=[]
        i=1
        while i**2<=n:
            li.append(i**2)
            i+=1

        to_check={n}
        count=0

        while to_check:
            count+=1
            next_check = set()
            
            for remainder in to_check:
                for square in li:
                    if remainder == square :
                        return count

                    if remainder < square:
                        break
                    
                    next_check.add(remainder - square)
            to_check=next_check

        return count