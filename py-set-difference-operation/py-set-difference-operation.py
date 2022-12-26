# Enter your code here. Read input from STDIN. Print output to STDOUT
num_eng = int(input())
english = set(input().split())
__ = input()
french = set(input().split())
print(len(english.difference(french)))
