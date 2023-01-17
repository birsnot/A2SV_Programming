num = input()
invert = {'5', '6', '7', '8', '9'}
ans = []
if num[0] == "9":
    ans.append("9")
elif num[0] in invert:
    ans.append(str(9-int(num[0])))
else:
    ans.append(num[0])
for digit in num[1:]:
    if digit in invert:
        ans.append(str(9-int(digit)))
    else:
        ans.append(digit)
if num == "0":
    print("9")
else:
    print("".join(ans))
