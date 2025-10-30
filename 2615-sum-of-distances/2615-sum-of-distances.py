from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic=defaultdict(list)
        answer=[0]*len(nums)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        for j in dic:
            k=len(dic[j])
            if k<2:
                continue
            total_sum=sum(dic[j])
            first_index=dic[j][0]
            current_distance=total_sum-(k*first_index)
            answer[dic[j][0]]=current_distance

            for z in range(k-1):
                delta = dic[j][z+1]-dic[j][z]
                left_group_count = z + 1
                right_group_count = k - (z + 1)


                current_distance = current_distance + delta * (left_group_count - right_group_count)
                answer[dic[j][z+1]] = current_distance
        return answer