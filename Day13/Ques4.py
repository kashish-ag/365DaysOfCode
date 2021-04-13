#Question link: https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st=s.split()
        st=st[:k]
        s=""
        for i in st:
            s+=i+" "
        return s[:-1]
