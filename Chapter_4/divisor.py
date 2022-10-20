# 2501 : divisor search
from sys import stdin
input = stdin.readline


def solve(N,S):
    cnt =0
    for i in range(1,N+1):
        if(N%i == 0):
            cnt += 1
        if(cnt == S):
            return i
    return 0


N,S = map(int,input().split())
print(solve(N,S))