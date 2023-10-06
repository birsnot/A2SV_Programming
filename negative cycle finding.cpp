// author: Nardos Wehabe

#include <bits/stdc++.h>

using namespace std;

long long dis[2500];
bool checked[2500];
int parent[2500];
int color[2500];
long long pf[2500];

void solve()
{
    int N, M;
    cin >> N >> M;
    vector<array<int, 3>> edges(M);
    vector<array<int, 2>> graph[N];

    int u, v, w;
    for (int i = 0; i < M; ++i)
    {
        cin >> u >> v >> w;
        u--;
        v--;
        edges[i] = {u, v, w};
        graph[u].push_back({v, w});
    }

    fill(dis, dis + N, LLONG_MAX);
    memset(checked, 0, sizeof checked);

    function<int(int)> check = [&](int st)
    {
        dis[st] = 0;
        bool updated;
        for (int i = 1; i < N; ++i)
        {

            updated = false;
            for (auto [u, v, w] : edges)
            {
                if (dis[u] != LLONG_MAX && dis[u] + w < dis[v])
                {
                    dis[v] = dis[u] + w;
                    updated = true;
                }
            }
            if (!updated)
                break;
        }
        if (updated)
        {
            for (auto [u, v, w] : edges)
            {
                if (dis[u] != LLONG_MAX && dis[u] + w < dis[v])
                {
                    return -1;
                }
            }
        }
        int ret = -2;
        for (int i = st + 1; i < N; ++i)
        {
            if (dis[i] != LLONG_MAX)
            {
                checked[i] = 1;
            }
            else
            {
                ret = 1;
            }
        }
        return ret;
    };

    memset(color, 0, sizeof color);
    memset(pf, 0ll, sizeof pf);

    function<int(int, long long)> dfs = [&](int v, long long path)
    {
        color[v] = 1;
        pf[v] = path;
        for (auto [ch, w] : graph[v])
        {
            if (color[ch] == 1 && pf[ch] > path + w)
            {
                parent[ch] = ch;
                return v;
            }
            if (color[ch] == 0 || pf[ch] > path + w)
            {
                parent[ch] = v;
                int res = dfs(ch, path + w);
                if (res != -1)
                    return res;
            }
        }
        color[v] = 2;
        return -1;
    };

    for (int i = 0; i < N; ++i)
    {
        if (checked[i])
            continue;
        int result = check(i);
        if (result == -2)
        {
            cout << "NO\n";
            return;
        }
        if (result == -1)
        {
            cout << "YES\n";
            int v = dfs(i, 0ll);
            vector<int> ans;
            while (parent[v] != v)
            {
                ans.push_back(v);
                v = parent[v];
            }
            ans.push_back(v);
            ans.push_back(ans[0]);
            reverse(ans.begin(), ans.end());
            for (auto n : ans)
                cout << n + 1 << " ";
            cout << "\n";
            return;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int tt = 1;

    // cin >> tt;

    while (tt--)
    {
        solve();
    }

    return 0;
}
