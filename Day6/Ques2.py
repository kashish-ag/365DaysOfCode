#Question Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            count=0
            for j in nums:
                if(j<i):
                    count=count+1
            l.append(count)
        return l
