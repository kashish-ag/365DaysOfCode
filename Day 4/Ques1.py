#Question Link: https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lent = len(nums)
        last = lent -1;
        
        if target < nums[0]:
            return 0
        elif target> nums[last]:
            return last +1
        pos = -1
        for i in range(lent):
            if nums[i] == target:
                pos = i;
        if pos != -1:
            return pos
        else:
            for i in range(lent):
                if nums[i]>=target:
                    return i
        
