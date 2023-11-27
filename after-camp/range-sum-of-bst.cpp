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
    int ans, low, high;
    int rangeSumBST(TreeNode* root, int low, int high) {
        this->low = low;
        this->high = high;
        ans = 0;
        calc(root);
        return ans;
    }
    void calc(TreeNode* root) {
        if(root == NULL) return;
        if(root->val >= low && root->val <= high) ans += root->val;
        if(root->val > low) calc(root->left);
        if(root->val < high) calc(root->right);
    }
};