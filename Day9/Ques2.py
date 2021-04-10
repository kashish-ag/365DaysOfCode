#Question Link:https://leetcode.com/problems/jewels-and-stones/ 

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l=[0]*len(jewels)
        i=0
        count=0
        while(i!=(len(jewels))):
            l[i]=jewels[i]
            i=i+1
        for i in range(len(stones)):
            if stones[i] in l:
                count=count+1
        return count
