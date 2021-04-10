#Question Link: https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0]* n
        
        for i in range(n):
            nums[i]=start+2*i
        op=0
        for i in nums:
            op=op^i
        return op
