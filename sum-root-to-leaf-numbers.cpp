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
    void dfs(TreeNode* node, int cur){
        cur = cur*10 + node->val;
        if(!node->right && !node->left){
            ans += cur;
            return;
        }
        if (node->right) dfs(node->right, cur);
        if (node->left) dfs(node->left, cur);
    }
    int sumNumbers(TreeNode* root) {
        dfs(root, 0);
        return ans;
    }
private:
    int ans = 0;
};