#약수의 개수를 구하시오
import sys
from xmlrpc.client import MAXINT
input = sys.stdin.readline

def solve(N,M):
    max_cnt = 0
    max_int = N
    for i in range(N,M+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if(i%j==0):
                cnt +=2
            if(j**2==i):
                cnt -=1
        if(cnt>=max_cnt):
            max_cnt=cnt
            max_int=i
    print(max_int)
    print(max_cnt)


N,M = map(int,input().split())
solve(N,M)