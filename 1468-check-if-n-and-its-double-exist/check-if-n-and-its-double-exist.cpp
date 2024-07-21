class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int,int> d;
        for (int i : arr) {
        if (d.find(i * 2) != d.end() || (i % 2 == 0 && d.find(i / 2) != d.end())) {
            return true;
        }
        d[i] = 1;
    }
    return false;
    }
};