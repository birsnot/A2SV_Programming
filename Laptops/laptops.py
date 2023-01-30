n = int(input())
laptops = []
for _ in range(n):
    laptops.append(tuple(map(int, input().split())))

laptops.sort()
answer = "Poor Alex"
prev = laptops[0][1]
for _, q in laptops:
    if q < prev:
        answer = "Happy Alex"
        break
    prev = q
print(answer)
