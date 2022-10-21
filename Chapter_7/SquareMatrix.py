import sys
input = sys.stdin.readline
def mult(b,m,k):
    n=len(b)
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for t in range(n):
                c[i][j] += (b[i][t] * m[t][j])
            c[i][j] %= k
    return c

def power(L,e,k):
    if(e==1):
        return L

    tmp = power(L,e//2,k)

    
    if(e%2==0):
        return mult(tmp , tmp,k)
    else:
        return mult(L, mult(tmp,tmp,k),k)

def solve(L,K,P):
    A = power(L,P,K)
    return A


N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
K,P = map(int,input().split())
A = solve(L, K,P)

for i in range(N):
    print(" ".join(map(str,A[i])))