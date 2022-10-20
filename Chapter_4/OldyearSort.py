#10814 : OldyearSorted
import sys
input= sys.stdin.readline

N=int(input())

L = [tuple(map(str,input().split())) for _ in range(N)]

L.sort(key=lambda x: (int(x[0])))

for i in range(len(L)):
    print(L[i][0], L[i][1])


