# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = tuple(map(int, input().split()))
words = {}
for i in range(1,n+1):
    word = input()
    if word in words:
        words[word].append(i)
    else:
        words[word] = [i]
for _ in range(m):
    word = input()
    if word in words:
        print(*words[word])
    else:
        print("-1")
