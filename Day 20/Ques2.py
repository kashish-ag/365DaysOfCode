#Question Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if n==1:
            return [0]
        elif n%2==0:
            for i in range(-n//2,0):
                ans.append(i)
            for i in range(1,(n//2)+1):
                ans.append(i)
            return ans
        else:
            for i in range((-n//2)+1,(n//2)+1):
                ans.append(i)
        return ans
