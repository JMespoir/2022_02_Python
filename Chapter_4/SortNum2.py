#2751 : SortNum2
from sys import stdin
input = stdin.readline

N = int(input())

A = [int(input()) for _ in range(N)]
A.sort()
for i in range(N):
    print(A[i])