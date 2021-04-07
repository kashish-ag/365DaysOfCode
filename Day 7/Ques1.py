#Question Link: https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        for i in items:
            if ruleKey=="type":
                if ruleValue==i[0]:
                    count=count+1
            if ruleKey=="color":
                if ruleValue==i[1]:
                    count=count+1
            if ruleKey=="name":
                if ruleValue==i[2]:
                    count=count+1
        return count
