#question Link:https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        summ=[0]*len(accounts)
        k=0
        for i in accounts:
            summ[k]=0
            for j in i:
                summ[k]=summ[k]+j
            k=k+1
        return max(summ)
            
