#Quetion Link: https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = dict()
        
        for ch in A[0]:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
                
        for k in d:
            for word in A[1:]:
                cnt = word.count(k)
                if cnt < d[k]:
                    d[k] = cnt
                    
        commonChars = []
        
        for k in d:
            if d[k] > 0:
                commonChars += [k] * d[k]
                
        return commonChars
