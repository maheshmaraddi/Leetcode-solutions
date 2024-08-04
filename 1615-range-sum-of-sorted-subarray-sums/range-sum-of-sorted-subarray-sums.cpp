class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        const int MOD = 1e9 + 7
        ;int ans=0
        ;vector<int>l;
        for(int i =0;i<n;i++){
            int s=0
            ;for (int j =i;j<n;j++){
                s+=nums[j]
                ;l.push_back(s)
            ;}
        }
        sort(l.begin(),l.end())
        ;for(int i=left-1;i<right;i++){
            ans=(ans+l[i])%MOD
        ;}
        return ans
   ; }

};