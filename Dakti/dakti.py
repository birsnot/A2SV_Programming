T = int(input())
for _ in range(T):
    str = input()
    i = 0
    nums =[]
    words = []
    word = ""
    while i < len(str):
        if str[i].isdigit():
            j = i 
            while j < len(str) and str[j].isdigit():
                j += 1
            nums.append(int(str[i:j]))
            i = j-1
        elif str[i] == " ":
            words.append(word)
            word = ""
        else:
            word += str[i]
        i += 1
    if word != "":
        words.append(word)
    ans = []
    for i in sorted(range(len(nums)),key=lambda x:nums[x]):
        ans.append(words[i])
    print(*ans)
