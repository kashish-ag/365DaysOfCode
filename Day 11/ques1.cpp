#Question Link: https://leetcode.com/problems/to-lower-case/ 

class Solution {
public:
    string toLowerCase(string str) {
        string s;
        transform(str.begin(), str.end(), str.begin(), ::tolower);
        return str;
    }
};
