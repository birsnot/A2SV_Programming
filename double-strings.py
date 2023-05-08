from collections import defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    ss = defaultdict(list)
    ss_set = set()
    for i in range(N):
        s = input()
        ss[s].append(i)
        ss_set.add(s)
    ans = ["0"]*N
    for s in ss:
        s_len = len(s)
        for i in range(1, s_len):
            s1, s2 = s[:i], s[i:]
            if s1 in ss_set and s2 in ss_set:
                for j in ss[s]:
                    ans[j] = "1"
    print("".join(ans))