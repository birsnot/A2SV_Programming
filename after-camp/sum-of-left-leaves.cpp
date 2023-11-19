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
    int sumOfLeftLeaves(TreeNode* root) {
        return calc(root, false);
    }
    int calc(TreeNode* root, bool is_left){
        if(root->left == nullptr && root->right == nullptr) return root->val*is_left;
        int ret = 0;
        if(root->left != nullptr) ret += calc(root->left, true);
        if(root->right != nullptr) ret += calc(root->right, false);
        return ret;
    }
};