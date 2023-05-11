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
    int ans = INT_MIN;
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }
    int dfs(TreeNode* node){
        int cur = 0, l = 0, r = 0;
        if(node->left) l = dfs(node->left);
        if(node->right) r = dfs(node->right);
        ans = max(ans, node->val + r + l);
        cur = node->val + max(l, r);
        return max(cur, 0);
    }
};