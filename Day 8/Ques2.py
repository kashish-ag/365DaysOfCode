#Question Link: https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st=[0]*len(indices)
        j=0
        for i in s:
            st[indices[j]]=i
            j=j+1
        ans=""
        for i in st:
            ans+=i
        return ans
