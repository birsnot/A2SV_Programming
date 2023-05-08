from collections import Counter, defaultdict


N, M = map(int, input().split())
prices = sorted(map(int, input().split()))
toys = defaultdict(int)
for _ in range(M):
    toys[input()] += 1
toys = Counter(toys)
toys = toys.most_common()
min_ = 0
max_ = 0
p1 = 0
p2 = N - 1
for _, fq in toys:
    min_ += prices[p1]*fq
    max_ += prices[p2]*fq
    p1 += 1
    p2 -= 1
print(min_, max_)