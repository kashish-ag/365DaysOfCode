#Question Link: https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = []
        out.append(first)
        
        for i in range(len(encoded)):
            n = encoded[i]^out[i]
            out.append(n)
        return out
