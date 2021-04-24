#Question Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in grid:
            for j in i:
                if j<0:
                    c+=1
        return c
