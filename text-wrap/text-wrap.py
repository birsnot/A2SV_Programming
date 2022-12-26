import textwrap

def wrap(string, max_width):
    loops = (len(string)//max_width)*max_width
    count = 0
    for ch in string[:loops]:
        count += 1
        print(ch, end="")
        if count == max_width:
            print()
            count = 0
    return string[loops:]
            
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
