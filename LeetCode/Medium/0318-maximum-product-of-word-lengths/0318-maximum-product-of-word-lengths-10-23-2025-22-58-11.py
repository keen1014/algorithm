from itertools import combinations
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        answer=[]
        for i in combinations(words, 2):
            tmp1, tmp2=i
            for j in range(len(tmp1)):
                if tmp1[j] in tmp2:
                    break
            else:
                answer.append(len(tmp1)*len(tmp2))
        print(answer)
        if answer:
            return max(answer)
        return 0