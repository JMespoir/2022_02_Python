# 1181 : Word Sort

from sys import stdin
input = stdin.readline

N = int(input())

A = []

for i in range(N):
    A.append(input().strip())

A=list(set(A))
A.sort(key=lambda x: (len(x),x))

for i in range(len(A)):
    print(A[i])