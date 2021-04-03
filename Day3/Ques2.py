#Question from Biweekly Contest. Link: https://leetcode.com/problems/count-nice-pairs-in-an-array/
class Solution:
       
    def countNicePairs(self, nums: List[int]) -> int:
        count=0
          
        for i in range(0,len(nums)):  
            
            for j in range(i+1,len(nums)):
                if i<j and j<len(nums):
                    rev1=0
                    x=nums[j]
                    while(x>0):
                        digit=x % 10
                        rev1=rev1*10+digit
                        x=int(x/10)
                    rev2=0
                    y=nums[i]
                    while(y>0):
                        digit=y % 10
                        rev2=rev2*10+digit
                        y=int(y/10)               
                    if(nums[i] + rev1) == (nums[j] + rev2):
                        count=count+1
        return count%1000000007
                        
             
