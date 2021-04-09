#Question Link: https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(0,len(nums),2):
            l1=[]
            while(nums[i]!=0):
                l1.append(nums[i+1])
                nums[i]=nums[i]-1
            l=l+l1
        return l
                
        
