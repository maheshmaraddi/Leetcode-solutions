class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_map<int,int>d;
        vector<int> ans;
        for(int i:nums){
            d[i]++;
        }
        for(auto i:d){
            if (i.second ==2){
                ans.push_back(i.first);
            }
        }
        return ans;
    }
};