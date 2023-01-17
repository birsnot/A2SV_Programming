a, b, ab = list(map(int, input().split()))
print(2*ab + min(abs(a-b),1)+2*min(a,b))
