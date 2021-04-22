#Question Link:https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=0
        for i in range(0,len(nums)-1):
            if (nums[i]>=nums[i+1]):
                n+=1+(nums[i]-nums[i+1])
                nums[i+1]=nums[i]+1
               
        
        return n
