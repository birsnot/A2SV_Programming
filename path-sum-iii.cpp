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
    int pathSum(TreeNode* root, int targetSum) {
        if(root == nullptr) return 0;
        return get_count(root, targetSum) + pathSum(root->left, targetSum) + pathSum(root->right, targetSum);
    }

    int get_count(TreeNode* node, long long target){
        target -= node->val;
        if(node->left == nullptr && node->right == nullptr){
            return (int)(target == 0);
        }
        int ret = (int)(target == 0);
        if(node->right != nullptr) ret += get_count(node->right, target);
        if(node->left != nullptr) ret += get_count(node->left, target);
        return ret;
    }
};