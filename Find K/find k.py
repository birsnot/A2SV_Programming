T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    nums = sorted(map(int, input().split()))
    ans = "NO"
    check1 = set()
    check2 = set()
    for n in nums:
        if n in check1 or n in check2:
            ans = "YES"
            break
        else:
            check1.add(K+n)
            check2.add(n-K)
    print(ans)
