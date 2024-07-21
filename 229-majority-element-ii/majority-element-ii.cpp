class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
           int n = floor(nums.size()/3)
           ;vector<int>res
           ;map<int,int>d
           ;for(int i:nums)
           {d[i]++;}
           for(auto i:d)
           {if(i.second >n)res.push_back(i.first);}
        return res;
    }
};