T = int(input())
for _ in range(T):
    tshirt1, tshirt2 = input().split()
    end1 = tshirt1[-1]
    end2 = tshirt2[-1]
    len_1 = len(tshirt1)
    len_2 = len(tshirt2)
    if end1 == end2:
        if end1 == "L":
            if len_1 > len_2:
                print(">")
            elif len_1 < len_2:
                print("<")
            else:
                print("=")
        elif end1 == "S":
            if len_1 < len_2:
                print(">")
            elif len_1 >len_2:
                print("<")
            else:
                print("=")
        else:
            print("=")
    elif end1 == "S":
        print("<")
    elif end1 == "L":
        print(">")
    else:
        if end2 == "S":
            print(">")
        else:
            print("<")
