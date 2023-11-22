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
    TreeNode* deleteNode(TreeNode* node, int key) {
        if(node == NULL) return NULL;
        if(node->val == key){
            if(node->right == NULL) return node->left;
            TreeNode *prev, *next = node->right;
            if(next->left == NULL){
                next->left = node->left;
                return next;
            }
            while(next->left != NULL){
                prev = next;
                next = next->left;
            }
            node->val = next->val;
            prev->left = next->right;
            return node;
        }
        if(key < node->val){
            node->left = deleteNode(node->left, key);
            return node;
        }
        node->right = deleteNode(node->right, key);
        return node;
    }
};