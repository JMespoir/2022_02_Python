#2609 : GCD and LCM
import sys
input = sys.stdin.readline
def solve(N,M):
    if(M==0):
        return N
    else:
        return solve(M, N%M)



N, M = map(int,input().split())

gcd = solve(N,M) if N>=M else solve(M,N)
lcm = (N*M)//gcd
print(gcd)
print(lcm)