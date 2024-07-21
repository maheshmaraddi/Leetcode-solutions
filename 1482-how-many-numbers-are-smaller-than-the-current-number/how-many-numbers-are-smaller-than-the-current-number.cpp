class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> c =nums;
        sort(c.begin(),c.end());
        vector<int> res;

        for(auto i :nums){
            auto it = find(c.begin(),c.end(),i);
            int ind = distance(c.begin(),it);
            res.push_back(ind);
        }
        return res;
    }
};