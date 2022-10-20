# 2750: SortNum

N = int(input())
A = []
for i in range(N):
    A.append(int(input())) #A = [int(input()) for _ in range(N)]

A.sort()
for i in range(N):
    print(A[i])