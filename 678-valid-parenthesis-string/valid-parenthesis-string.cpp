class Solution {
public:
    bool checkValidString(string s) {        
        int left = 0, right = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '(' || s[i] == '*') left++;
            else left--;

            if(s[s.length()-1-i] == ')' || s[s.length()-1-i] == '*') right++;
            else right--;

            if(left < 0 || right < 0) return false;
        }
        return true;
    }
};