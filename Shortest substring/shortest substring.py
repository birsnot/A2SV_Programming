T = int(input())
for _ in range(T):
    s = input()
    one = -1
    two = -1
    three = -1
    ans = len(s) + 1
    for i, ch in enumerate(s):
        if ch == "1":
            one = i
        elif ch == "2":
            two = i
        elif ch == "3":
            three = i
        if -1 not in [one, two, three]:
            temp = max(one, two, three) - min(one, two, three)
            ans = min(ans, temp)
    if -1 in [one, two, three]:
        print(0)
    else:
        print(ans + 1)
