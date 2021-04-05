#Question Link:https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[0]*len(nums)
        j=0
        for i in range(0,n):
            l[j]=nums[i]
            l[j+1]=nums[i+n]
            j=j+2
        return l
