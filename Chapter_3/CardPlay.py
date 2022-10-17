# 4564 : number card play
def solve (s):
    print(s, end =" ")
    if s//10 == 0:
        return print()
    sum = 1
    while(s >=1):
        sum *= (s%10)
        s //=10
    return solve(sum)
while(True):
    S = int(input())
    if(S == 0):
        break
    solve(S)