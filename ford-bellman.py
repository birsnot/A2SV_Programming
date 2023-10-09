// author: Nardos Wehabe

#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int N, M;
    cin >> N >> M;
    vector<array<int, 3>> edges(M);
    for (int i = 0; i < M; ++i)
    {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
        edges[i][0]--;
        edges[i][1]--;
    }

    vector<int> dis(N, 30000);

    dis[0] = 0;
    for (int i = 0; i < N; ++i)
    {
        for (auto [u, v, w] : edges)
        {
            if (dis[u] < 30000 && dis[u] + w < dis[v])
                dis[v] = dis[u] + w;
        }
    }
    for (auto n : dis)
        cout << n << " ";
    cout << "\n";
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