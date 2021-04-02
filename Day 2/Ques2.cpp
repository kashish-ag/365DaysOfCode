//question link:https://leetcode.com/problems/reverse-integer/
//solution:

class Solution {
public:
    long long int reverse(long long int x) {
         
        if(x<0){
            long long int digit;
            long long int rev=0;
            x=x*(-1);
            while(x>0){
                digit=x%10;
                rev=rev*10+digit;
                if(rev>2147483647){
                    return 0;
                }
                x=x/10;
            }
            return -rev;
        }
        else{
            long long int digit;
            long long int rev=0;
            while(x>0){
                digit=x%10;
                rev=rev*10+digit;
                if(rev>2147483647){
                    return 0;
                }
                x=x/10;
            }
            return rev;        
        }
    }
};
