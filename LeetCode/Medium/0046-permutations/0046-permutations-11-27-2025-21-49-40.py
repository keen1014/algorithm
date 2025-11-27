from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        for i in permutations(nums, len(nums)):
            answer.append(list(i))
        return answer