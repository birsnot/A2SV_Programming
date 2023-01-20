n, k = list(map(int, input().split()))
seq = sorted(map(int, input().split()))
if n == k:
    print(seq[k-1])
elif k == 0:
    if seq[0] > 1:
        print(1)
    else:
        print(-1)
elif seq[k] != seq[k-1]:
    print(seq[k-1])
elif seq[k] == seq[k-1]:
    print(-1)
