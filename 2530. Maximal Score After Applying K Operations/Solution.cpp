class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) 
    {
        long long ans = 0LL;
        priority_queue<int>q;
        for(auto c : nums)
        {
            q.push(c);
        }
        while(k--)
        {
            int temp = q.top();
            q.pop();
            ans+=static_cast<long long>(temp);
            temp = ceil(static_cast<double>(temp)/3.0);
            q.push(temp);
        }
        return ans;
    }
};
