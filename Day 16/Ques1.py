#Question:https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        c=0
        while(n>1):
            if (n%2==0):
                c+=n//2
                n=n//2
                
            else:
                c+=(n-1)//2
                n=(n-1)//2+1
               
        return c
