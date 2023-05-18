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
    int sumEvenGrandparent(TreeNode* root) {
        return summer(root, 1, 1);
    }
    int summer(TreeNode* root, int gp, int p){
        if (root == NULL) return 0;
        int l = summer(root->left, p, root->val);
        int r = summer(root->right, p, root->val);
        return l + r + (gp%2 == 0)*root->val;
    }
};