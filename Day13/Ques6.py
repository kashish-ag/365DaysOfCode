#Question Link: https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
       
        l=[]
        while(num>0):
            digits=num%10
            l.append(digits)
            num=int(num/10)
        l.reverse()
        for i in range(len(l)):
            if l[i]==6:
                l[i]=9
                break
        num=0
        j=len(l)-1
        for i in l:
            num+=i*(10**j)
            j=j-1
        return num
