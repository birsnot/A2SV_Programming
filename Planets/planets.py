from collections import Counter


T = int(input())
for _ in range(T):
    n, c = list(map(int,input().split()))
    orbits = Counter(input().split())
    ans = 0
    for planets in orbits.values():
        ans += min(planets, c)
    print(ans)
