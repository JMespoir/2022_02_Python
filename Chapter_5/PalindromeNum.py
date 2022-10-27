#1259 : palindromeNum
import sys
input = sys.stdin.readline

def solve(A):
    longA=len(A)
    for i in range(longA//2):
        if(A[i] != A[longA-1-i]):
            return "no"
    return "yes"

A = input().strip()

while(A[0] != '0'):
    print(solve(A))
    A = input().strip()
