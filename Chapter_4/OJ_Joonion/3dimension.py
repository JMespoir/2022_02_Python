#3차원 좌표 정렬하기

N = int(input())
ary = [tuple(map(int,input().split())) for _ in range(N)]
ary.sort(key=lambda x: (x[0],-x[1],x[2]))
for i in range(N):
    print(" ".join(map(str,ary[i])))