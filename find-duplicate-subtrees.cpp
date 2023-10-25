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
    vector<TreeNode*> ans;
    unordered_map<string, int> hash;
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        dfs(root);
        return ans;
    }
    string dfs(TreeNode* node){
        if(node == nullptr) return "n";
        string ret = to_string(node->val);
        ret += "|" + dfs(node->left);
        ret += "|" + dfs(node->right);
        if(hash.count(ret)){
            if(hash[ret] != -1){
                ans.push_back(node);
                hash[ret] = -1;
            }
        }
        else hash[ret] = 1;
        return ret;
    }
};