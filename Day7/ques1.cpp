//Question Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution {
public:
    int subtractProductAndSum(int n) {
        int digits, sum=0,prod=1;
        while(n>0){
            digits=n%10;
            sum+=digits;
            prod*=digits;
            n=n/10;
        }
        return prod-sum;
    }
};
