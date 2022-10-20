#5618 : Common divisor
import sys
input = sys.stdin.readline

def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n%m)

def solve(N,L):
    m = gcd(L[0],L[1])
    if(N==3):
        m = gcd(m,L[2])
    K = divisor(m)
    for i in range(len(K)):
        print(K[i])

def divisor(m):
    A = []
    for i in range(1,int(m**0.5)+1):
        if(m%i==0):
            A.append(i)
            A.append(m//i)
    A = list(set(A))
    A.sort()
    return A


N = int(input())
L = list(map(int,input().split()))

solve(N,L)
