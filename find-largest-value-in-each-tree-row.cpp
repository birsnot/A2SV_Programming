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
    vector<int> largestValues(TreeNode* root) {
        if(root == nullptr) return vector<int>();
        vector<int> ans;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int max_ = INT_MIN, L = q.size();
            for(int i = 0; i < L; ++i){
                TreeNode* cur = q.front(); q.pop();
                if(cur->val > max_) max_ = cur->val;
                if(cur->left != nullptr) q.push(cur->left);
                if(cur->right != nullptr) q.push(cur->right);
            }
            ans.push_back(max_);
        }
        return ans;
    }
};