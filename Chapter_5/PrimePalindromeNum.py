#1747 : prime && palindrome

import sys
input = sys.stdin.readline
def isPrime(N):
    if(N<2 or (N !=2 and N %2 == 0)):
        return False
    else:
        for t in range(2, int(N**0.5)+1):
            if(N%t==0):
                return False
        return True

def isPalindrome(N):
    s = str(N)
    longs=len(s)
    for i in range(longs//2):
        if(s[i] != s[longs-1-i]):
            return False
    return True

def Solve(N):
    while(True):
        if(isPrime(N) and isPalindrome(N)):
            return N
        N+=1

N = int(input())
print(Solve(N))
