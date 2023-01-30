T = int(input())
for _ in range(T):
    s = input()
    s_len = len(s)
    if s_len == 1:
        print(s)
        continue
    i = 0
    j = 1
    ans = set()
    while j < s_len:
        if s[j] != s[i]:
            ans.add(s[i])
            j += 1
            i += 1
        else:
            i += 2
            j += 2
    if i < s_len:
        ans.add(s[i])
    print("".join(sorted(ans)))
