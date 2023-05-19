// autor: birsnot - Nardos Wehabe

#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int N, M; 
    cin >> N >> M;
    vector<pair<int, int>> from[N + 1];
    vector<pair<int, int>> to[N + 1];
    int u, v;
    for(int i = 0; i < M; ++i){
        cin >> u >> v;
        from[u].push_back(make_pair(v, i));
        to[v].push_back(make_pair(u, i));
    }
    vector<int> ans(M);
    vector<int> color(N + 1);
    int source = 1, sink = 2;
    int state[2] = {0, 1};
    function<bool(int, int)> dfs = [&](int v, int prev){
        color[v] = prev^3;
        for(auto ch: from[v]){
            int u = ch.first, i = ch.second;
            ans[i] = state[color[v] == source];
            if(color[u] == 0){
                if(!dfs(u, color[v])){
                    return false;
                }
            }
            else if(color[u] == color[v]) return false;
        }
        for(auto ch: to[v]){
            int u = ch.first, i = ch.second;
            ans[i] = state[color[v] == sink];
            if(color[u] == 0){
                if(!dfs(u, color[v])) return false;
            else if (color[u] == color[v]) return false;
            }
        }
        return true;
    };
    
    for (int i = 1; i <= N; ++i){
        if(color[i] == 0){
            if(!dfs(i, 1)){
                cout << "NO\n";
                return;
            }
        }
    }
    cout <<"YES\n";
    for(int i = 0; i < M; ++i){
        cout<< ans[i];
    }
    cout <<"\n";




}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int tt;
    // cin >> tt;
    tt = 1;
    while (tt--)
    {
        solve();
    }
    return 0;
}
