#Question Link: https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.insert(index[i],nums[i])
        return l
