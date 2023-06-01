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
public:
    int rob(TreeNode* root) {
        auto ans = helper(root);
        return max(ans.first, ans.second);
    }
    pair<int,int> helper(TreeNode* node){
        int left_prev1 = 0, left_prev2 = 0, right_prev1 = 0, right_prev2 = 0;
        if(node->left){
            auto left = helper(node->left);
            left_prev1 = left.first;
            left_prev2 = left.second;
        }
        if(node->right){
            auto right = helper(node->right);
            right_prev1 = right.first;
            right_prev2 = right.second;
        }
        int cur = max(node->val + left_prev1 + right_prev1, left_prev2 + right_prev2);
        return {left_prev2 + right_prev2, cur};
    }
};