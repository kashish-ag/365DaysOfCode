#Question Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        lent = len(candies)
        candy = [1] * lent
        maxi = 0
        for i in range(lent):
            if candies[i]>=maxi:
                maxi = candies[i] #works
        for i in range(lent):
            candies[i] = candies[i]+extraCandies
        for i in range(lent):
            if candies[i]<maxi:
                candy[i] = 0
        return candy
        
        
