//question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
//solution:

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==0){
            return 0;
        }
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]==nums[i+1]){
                nums.erase(nums.begin()+i);
                i--;
            }
            else{
                continue;
            }
        }
        return nums.size();
    }
};
