#question link:https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(min(len(word1), len(word2))):
            result.extend([word1[i], word2[i]])
                       
        if len(word1) < len(word2):
            long = word2
        else:
            long = word1
                       
        result.extend(long[i+1:])
                       
        return "".join(result)
