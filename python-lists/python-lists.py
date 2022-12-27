if __name__ == '__main__':
    N = int(input())
    list_ = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            list_.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(list_)
        elif command[0] == "remove":
            list_.remove(int(command[1]))
        elif command[0] == "append":
            list_.append(int(command[1]))
        elif command[0] == "sort":
            list_.sort()
        elif command[0] == "pop":
            list_.pop()
        else:
            list_.reverse()
