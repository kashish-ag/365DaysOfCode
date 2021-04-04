#Question Link: https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        l[0]=nums[0]
        for i in range(1,len(nums)):
            l[i]=0
            for j in range(0,i+1):
                l[i]=l[i]+nums[j]
        return l
                
