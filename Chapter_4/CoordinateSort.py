#11650 :Coordinate Sort
from sys import stdin
input = stdin.readline


N = int(input())

A = [tuple(map(int,input().split())) for _ in range(N)]

A.sort()
for i in range(N):
    print(A[i][0], A[i][1])
