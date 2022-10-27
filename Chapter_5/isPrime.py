#1929 : GET Prime Num
import sys
input = sys.stdin.readline

def isPrime(i):
    if(i<2 or (i !=2 and i %2 == 0)):
        return False
    else:
        for t in range(2, int(i**0.5)+1):
            if(i%t==0):
                return False
        return True



def solve(m,n):
    for i in range(m,n+1):
        if(isPrime(i)):
            print(i)


M,N = map(int,input().split())

solve(M,N)