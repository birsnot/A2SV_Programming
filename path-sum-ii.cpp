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
    vector<vector<int>> ans;
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if(root == nullptr) return vector<vector<int>>();
        if(!clean(root, targetSum)) return vector<vector<int>>();
        dfs(root, vector<int>());
        return ans;
    }

    bool clean(TreeNode* node, int target){
        target -= node->val;
        if(node->right == nullptr && node->left == nullptr){
            return target == 0;
        }
        bool cur = false;
        if(node->left != nullptr){
            if(!clean(node->left, target)) node->left = nullptr;
            else cur = true;
        }
        if(node->right != nullptr){
            if(!clean(node->right, target)) node->right = nullptr;
            else cur = true;
        }
        return cur;
    }

    void dfs(TreeNode *node, vector<int> path){
        path.push_back(node->val);
        if(node->right == nullptr && node->left == nullptr){
            ans.push_back(path);
            return;
        }
        if(node->left != nullptr){
            dfs(node->left, path);
        }
        if(node->right != nullptr){
            dfs(node->right, path);
        }
    }
};