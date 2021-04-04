#Question Link: https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no=0
        for i in digits:
            no=no*10+i
        no=no+1
        l=[]
        while(no>0):
            d=no%10
            l.append(d)
            no=no//10
        l1=[]
        n=len(l)-1
        for i in range(n,-1,-1):
            l1.append(l[i])
        return l1
