#Question:https://leetcode.com/problems/check-if-the-sentence-is-pangram/
import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_set = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet_set:
            if char not in sentence:
                return False
        return True
