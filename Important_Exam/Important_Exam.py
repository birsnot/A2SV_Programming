n, m = list(map(int, input().split()))
student_answers = []
for _ in range(n):
    student_answers.append(input())
marks = list(map(int, input().split()))
res = 0
for i in range(m):
    ans_count = {}
    for answer in student_answers:
        ans_count[answer[i]] = ans_count.get(answer[i], 0) + 1
    max_ans = 0
    for ans in ans_count:
        if ans_count[ans] > max_ans:
            max_ans = ans_count[ans]
    res += max_ans*marks[i]
print(res)
