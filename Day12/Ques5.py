#Question Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a=s[0:n//2]
        b=s[n//2:]
        v=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c1=0
        c2=0
        for i in a:
            if i in v:
                c1+=1
        for i in b:
            if i in v:
                c2+=1
        if c1==c2:
            return True
        return False
