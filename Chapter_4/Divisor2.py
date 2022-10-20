#1037 : Divisor2
import sys
input = sys.stdin.readline

def solve(N,L):
    if(N==1):
        return L[0]**2
    else:
        L.sort()
        return L[0] * L[-1]


N = int(input())
L = list(map(int,input().split()))
print(solve(N,L))