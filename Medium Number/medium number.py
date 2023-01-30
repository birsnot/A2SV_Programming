T = int(input())
for _ in range(T):
    a, b, c = list(map(int, input().split()))
    min_ = min(a, b, c)
    max_ = max(a, b, c)
    if a != min_ and a != max_:
        print(a)
    elif b != min_ and b != max_:
        print(b)
    else:
        print(c)
