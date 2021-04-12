#Question Link:https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[0]*(len(gain)+1)
        l[0]=0
        j=0
        for i in range(len(gain)):
            a=l[j]+gain[i]
            
            j=j+1
            l[j]=a
        return max(l)
