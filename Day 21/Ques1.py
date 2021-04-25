#Question Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/

def signFunc(x):
        if x>0:
            return 1
        elif x<0:
            return -1 
        else:
            return 0
class Solution:
    
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        for i in nums:
            prod*=i
        return (signFunc(prod))
