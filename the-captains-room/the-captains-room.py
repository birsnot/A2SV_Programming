# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
k = int(input())
rooms = input().split()
c = collections.Counter(rooms)
for r in c:
    if c[r] != k:
        print(r)
        break
