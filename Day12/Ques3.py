#Question Link: https://leetcode.com/problems/matrix-diagonal-sum/
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d1=0
        d2=0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if(i==j):
                    d1=d1+mat[i][j]
                
                if (i+j==n-1):
                    d2=d2+mat[i][j]
        if n%2==0:
            return d1+d2
        a=(n//2)
        b=mat[a][a]        
        return d1+d2-b
