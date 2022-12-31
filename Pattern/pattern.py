T = int(input())
words = []
for _ in range(T):
    words.append(input())
word_len = len(words[0])
ans = ""
for i in range(word_len):
    chars = set()
    for word in words:
        chars.add(word[i])
    if "?" in chars:
        if len(chars) > 2:
            ans += "?"
        elif len(chars) == 2:
            p = iter(chars)
            ch = next(p)
            if ch != "?":
                ans += ch
            else:
                ans += next(p)
        else:
            ans += "a"
    else:
        if len(chars) > 1:
            ans += "?"
        else:
            ans += next(iter(chars))
print(ans)
