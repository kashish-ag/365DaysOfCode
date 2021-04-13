#Question link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=max(nums)
        for i in range(len(nums)):
            if (nums[i]==max1):
                nums[i]=0
                break
        max2=max(nums)
        return (max1-1)*(max2-1)

