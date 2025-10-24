class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1,10000001):
            dic={'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,'6':0, '7':0,'8':0,'9':0}
            i=str(i)
            for j in range(len(i)):
                dic[i[j]]+=1
            for j in dic:
                if dic[j]!=0 and dic[j]==int(j):
                    continue
                elif dic[j]!=0 and dic[j]!=int(j):
                    break
            else:
                return int(i)