# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
nums = input().split()
happy = set(input().split())
sad = set(input().split())
ans = 0
for n in nums:
    if n in happy:
        ans += 1
    elif n in sad:
        ans -= 1
print(ans)
