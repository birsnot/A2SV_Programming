class Solution {
    class Node{
    public:
        Node *child[26];
        Node(){
            for(auto &ch: child) ch = nullptr;
        }
    };
    Node *root;
public:
    Solution(){
        root = new Node();
    }

    int insert(string &word){
        Node *cur = root;
        int idx, i = 0;
        char ch;
        for(; i < word.size(); ++i){
            ch = word[i];
            idx = ch - 'a';
            if(cur->child[idx] == nullptr){
                if(i == word.size() - 1){
                    i++;
                    cur->child[idx] = new Node();
                }
                return i;
            }
            cur = cur->child[idx];
        }
        return i;
    }

    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end(), [](const string a, const string b){
            return a.size() < b.size();
        });
        string ans;
        int end, max = 0;
        for(auto &word: words){
            end = insert(word);
            if(end > max){
                ans = word.substr(0, end);
                max = end;
            }
            else if(end == max){
                ans = min(ans, word.substr(0, end));
            }
        }
        return ans;
    }
};