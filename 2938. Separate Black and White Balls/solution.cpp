class Solution {
public:
    long long minimumSteps(string s) 
    {
        long long ans = 0;
        if(s.length() == 0 || s.length() == 1)
            return 0;
        int r = s.length()-1;
        long long count = 0LL;
        while(r>=0)
        {
            if(s[r] == '1')
                ans+=count;
            else
                count+=1LL;
            r--;
        }
        return ans;
    }
};
