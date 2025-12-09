class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        answer=0
        if len(nums1)%2==1:
            for i in nums2:
                answer^=i
        if len(nums2)%2==1:
            for j in nums1:
                answer^=j
        return answer