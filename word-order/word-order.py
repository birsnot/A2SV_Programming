# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = {}
for _ in range(n):
    key = input()
    words[key] = words.get(key, 0) + 1
print(len(words))
print(*words.values())
