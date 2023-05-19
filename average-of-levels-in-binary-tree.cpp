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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        queue<TreeNode*> dq;
        double sum, len;
        dq.push(root);
        while (!dq.empty()){
            len = dq.size();
            sum = 0;
            for(int i = 0; i < len; ++i){
                TreeNode *node = dq.front();
                dq.pop();
                sum += node->val;
                if(node->right) dq.push(node->right);
                if(node->left) dq.push(node->left);
            }
            ans.push_back(sum/len);
        }
        return ans;
    }
};