#Questions are from LeetCode Biweekly Contest. Link- https://leetcode.com/problems/determine-color-of-a-chessboard-square/
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        ch=coordinates[0]
        no=int(coordinates[1])
        odd=['a','c','e','g']
        even=['b','d','f','h']
        if(no%2==0):
            if (ch in even):
                return False
            if (ch in odd):
                return True
        else:
            if (ch in odd):
                return False
            if (ch in even):
                return True
        
