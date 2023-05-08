T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    a = sorted(input())
    b = sorted(input())
    c = []
    p1 = p2 = 0
    taken_from = "c"
    k = 0
    while p1 < N and p2 < M:
        if k < K:
            if a[p1] < b[p2]:
                c.append(a[p1])
                p1 += 1
                if taken_from == "a":
                    k += 1
                else:
                    taken_from = "a"
                    k = 1
            else:
                c.append(b[p2])
                p2 += 1
                if taken_from == "b":
                    k += 1
                else:
                    taken_from = "b"
                    k = 1
        else:
            if taken_from == "a":
                c.append(b[p2])
                taken_from = "b"
                p2 += 1
                k = 1
            else:
                c.append(a[p1])
                taken_from = "a"
                p1 += 1
                k = 1
    print("".join(c))