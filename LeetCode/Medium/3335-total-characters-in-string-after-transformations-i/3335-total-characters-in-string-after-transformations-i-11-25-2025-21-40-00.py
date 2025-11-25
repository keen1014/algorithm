class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counts=[0]*26
        answer=0
        MOD=10**9+7
        for i in s:
            counts[ord(i)-97]+=1
        

        for _ in range(t):
            tmp_a_b=counts[25]
            counts[25]=counts[24]
            counts[24]=counts[23]
            counts[23]=counts[22]
            counts[22]=counts[21]
            counts[21]=counts[20]
            counts[20]=counts[19]
            counts[19]=counts[18]
            counts[18]=counts[17]
            counts[17]=counts[16]
            counts[16]=counts[15]
            counts[15]=counts[14]
            counts[14]=counts[13]
            counts[13]=counts[12]
            counts[12]=counts[11]
            counts[11]=counts[10]
            counts[10]=counts[9]
            counts[9]=counts[8]
            counts[8]=counts[7]
            counts[7]=counts[6]
            counts[6]=counts[5]
            counts[5]=counts[4]
            counts[4]=counts[3]
            counts[3]=counts[2]
            counts[2]=counts[1]
            counts[1]=counts[0]
            counts[0]=0
            counts[0]+=tmp_a_b
            counts[1]+=tmp_a_b
        return sum(counts)%MOD
#26 1번돌면 2자리 ab
#52 2번 돌면 4자리 abbc
#78 3번 돌면 abbcbccd
#104 4번 돌면 abbcbccdbccdcdde