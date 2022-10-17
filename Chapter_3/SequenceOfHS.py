#3943 : HaleStone Sequence
from sys import stdin

def solve(N):
    max=1
    while(N!=1):
        if(max<N):
            max = N
        if(N %2 == 0):
            N //=2
        else:
            N =N*3 +1
    return max


T = int(stdin.readline())
for i in range(T):
    N = int(stdin.readline())
    print(solve(N))