#Question Link: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l=[]
        for i in rectangles:
            m=min(i)
            l.append(m)
        length=max(l)
        count=0
        for i in l:
            if(i==length):
                count+=1
        return count
