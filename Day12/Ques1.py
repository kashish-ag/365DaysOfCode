#Question Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        l=[0]*len(allowed)
        for i in range(len(allowed)):
            l.append(allowed[i])
        for i in words:
            flag=1
            for j in range(len(i)):
                if i[j] not in l: 
                    flag=0
            if flag==1:
                count=count+1
        return count
