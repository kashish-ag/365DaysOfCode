//question link: https://leetcode.com/problems/palindrome-number/
//accepted answer:


class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
        {
            return false;
        }
        else{
            int y,digit;
            unsigned int rev=0;
            y=x;
            while(x>0){
                digit=int(x%10);
                rev=rev*10+digit;
                x=int(x/10);
            }
            if(y==rev){
                return true;
            }
            return false;
        }
    }
};
