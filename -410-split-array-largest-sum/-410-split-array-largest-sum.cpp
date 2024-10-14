class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
    int s = 0, e = 0;
    for (int i = 0; i < nums.size(); i++) {
        s = max(s, nums[i]); // Find max element
        e += nums[i]; // Sum of all elements
    }
    while (s < e) {
        int mid = s + (e - s) / 2;
        int pieces = count(nums, mid);
        if (pieces <= k) {
            e = mid; // Try for a smaller max sum
        } else {
            s = mid + 1; // Increase the allowed max sum
        }
    }
    return e;
    }
    int count(const vector<int>& nums, int mid) {
    int sum = 0, pieces = 1;
    for (int i = 0; i < nums.size(); i++) {
        if (sum + nums[i] <= mid) {
            sum += nums[i];
        } else {
            sum = nums[i]; // Start a new piece
            pieces++;
        }
    }
    return pieces;
}
};