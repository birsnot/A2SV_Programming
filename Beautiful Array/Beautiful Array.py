from os import remove


n = int(input())
nums = list(map(int, input().split()))
negatives = []
positives = []
zero = []
for i,num in enumerate(nums):
    if num < 0:
        negatives.append(nums.pop(i))
        break
for num in nums:
    if num > 0:
        positives.append(num)
    else:
        zero.append(num)
if not positives:
    count = 0
    remove_ = []
    for num in zero:
        if num < 0:
            positives.append(num)
            remove_.append(num)
            count += 1
            if count == 2:
                break
    for num in remove_:
        zero.remove(num)
print(len(negatives), *negatives)
print(len(positives), *positives)
print(len(zero), *zero)
