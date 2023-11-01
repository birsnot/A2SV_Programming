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
    vector<TreeNode*> ans;

    bool dfs(TreeNode* node, unordered_set<int>& to_del){
        if(node == nullptr) return false;
        if(to_del.find(node->val) != to_del.end()){
            if(dfs(node->left, to_del)) ans.push_back(node->left);
            if(dfs(node->right, to_del)) ans.push_back(node->right);
            return false;
        }
        if(!dfs(node->left, to_del)){
            node->left = nullptr;
        }
        if(!dfs(node->right, to_del)){
            node->right = nullptr;
        }
        return true;
    }

    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> to_del(to_delete.begin(), to_delete.end());
        if(dfs(root, to_del)) ans.push_back(root);
        return ans;
    }
};