# Enter your code here. Read input from STDIN. Print output to STDOUT
superset = set(map(int, input().split()))
n = int(input())
ans = True
for _ in range(n):
    subset = set(map(int,input().split()))
    if subset.difference(superset) or len(subset) >= len(superset):
        ans = False
        break
print(ans)
