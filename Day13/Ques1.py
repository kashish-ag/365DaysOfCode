#Question Link: https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={}
        for i in paths:
            d[i[0]]=i[1]
        for k,v in d.items():
            if d.get(v) is None:
                return v
            
