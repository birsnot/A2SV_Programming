if __name__ == '__main__':
    n_list = []
    min1 = 101.0
    max
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < min1:
            min1 = score
        n_list.append([name,score])
    min2 = 101
    for i in n_list:
        if i[1] > min1:
            if i[1] < min2:
                min2 = i[1]
    names = []
    for i in n_list:
        if i[1] == min2:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
