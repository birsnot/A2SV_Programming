// autor: birsnot - Nardos Wehabe

#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int N, M;
    cin >> N >> M;
    vector<int> adj[N];
    int cost[N];
    for(int i = 0; i < N; ++i){
        cin >> cost[i];
    }
    int u, v;
    for(int i = 0; i < M; ++i){
        cin >> u >> v;
        --u, --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<bool> visited(N);
    function<int(int)> dfs = [&](int v){
        int ret = cost[v];
        visited[v] = true;
        for(auto ch: adj[v]){
            if(!visited[ch]){
                ret = min(ret, dfs(ch));
            }
        }
        return ret;
    };
    long long ans = 0;
    for(int i = 0; i < N; ++i){
        if(!visited[i]){
            ans += dfs(i);
        }
    }
    cout << ans << "\n";
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
