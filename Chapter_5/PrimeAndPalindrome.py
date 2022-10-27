#1990 : Prime and Palindrome
import sys
input = sys.stdin.readline
def makeprimes(N,M):
    cnt = M
    if(M>=10000000):
        cnt = 10000000
    a = [False,False] + [True]*(cnt-1)
    primes=[]
    for i in range(2,cnt+1):
        if a[i]:
            if(i>=N):
                primes.append(i)
            for j in range(2*i, cnt+1, i):
                a[j] = False
    return primes

def Palindrome(num):
    s = str(num)
    return s == s[::-1]

def solve(N,M):
    primes = makeprimes(N,M)
    for i in range(len(primes)):
        if(Palindrome(primes[i])):
            print(primes[i])
    print("-1")

N,M = map(int,input().split())
solve(N,M)
