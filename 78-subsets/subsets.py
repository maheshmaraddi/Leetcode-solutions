# void solve(vector<int> nums, vector<int> output , int index , vector<vector<int>> &ans){

#         if (index>=nums.size()){
#             ans.push_back(output);
#             return ;
#         }
#         solve(nums,output,index+1,ans);
#         int element= nums[index];
#         output.push_back(element);
#         solve(nums,output,index+1,ans);
#     }
# public:
#     vector<vector<int>> subsets(vector<int>& nums) {
#         vector<vector<int>> ans;
#         vector<int>output;
#         int index=0;
#         solve(nums,output,index,ans);
#         return ans;
#     }
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
        