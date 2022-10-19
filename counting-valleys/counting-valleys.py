def countingValleys(steps, path):
    # Write your code here 
    pos = 0
    move = {'D':-1, 'U':1}
    ans = 0
    for step in path:
        if pos == -1 and step == 'U':
            ans += 1
        pos += move[step]
    return ans
