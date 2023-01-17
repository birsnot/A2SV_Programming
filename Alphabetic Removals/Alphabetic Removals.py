n, k = list(map(int, input().split()))
chars = list(input())
letters = 'abcdefghijklmnopqrstuvwxyz'
remove = 0
done = False
while True:
    for i,char in enumerate(chars):
        if char == letters[remove]:
            chars[i] = 0
            k -= 1
            if k == 0:
                done = True
                break
    if done:
        break
    else:
        remove += 1
ans = []
for char in chars:
    if char != 0:
        ans.append(char)
print("".join(ans))
