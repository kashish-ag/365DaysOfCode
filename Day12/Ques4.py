#Question Link: https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        summ=0
        for k,v in d.items():
            if v==1:
                summ+=k
        return summ
