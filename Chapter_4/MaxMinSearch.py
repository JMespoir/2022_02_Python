#10818: MAX and MIN search
from sys import stdin
input = stdin.readline


N = int(input())
A = list(map(int, input().split()))
print(max(A), min(A))