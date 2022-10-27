# 14561 : Palindrome
import sys
input=sys.stdin.readline

def Palindrome(A,n):
    L = []
    L = returnN(A,n,L)
    for i in range(len(L)//2):
        if(L[i] != L[len(L)-1-i]):
            return 0
    return 1

def returnN(A,n,L):
    if(A==0):
        return L
    L.append(A%n)
    return returnN(A//N,n,L)

T = int(input())
for i in range(T):
    A,N = map(int,input().split())
    print(Palindrome(A,N))