/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int c=0;
    public :
    int fun(TreeNode* root){
        if(root==NULL){
            return 0;
        }
        else{
            int l=fun(root->left);
            int r=fun(root->right);
            c=c+abs(l) + abs(r);
            return root->val + l +r -1;
        }
    } 
public:
    int distributeCoins(TreeNode* root) {
        int a=fun(root);
        return c;
    }
};