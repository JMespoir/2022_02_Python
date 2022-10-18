#2270: HanoiTower2 미완
def solve(a,b,c,N,cnt):
    if(a[0]>b[0]):
        if(a[0]>c[0]):
            P = 1
            if(b[0]>c[0]): # b[0]> c[0]
                Q = Hanoi(cnt[1],cnt[2])
            else:#c[0]>b[0]
                Q = Hanoi(cnt[2],cnt[1])
        else: # c>a>b
            P = 3
            Q = Hanoi(cnt[0],cnt[1])
    else:
        if(b[0]>c[0]):#b>a?c
            P = 2
            if(a[0]>c[0]):#b>a>c
                Q = Hanoi(cnt[0],cnt[2])
            else:
                Q = Hanoi(cnt[2],cnt[1])
        else: # c>a<b
            P = 3
            Q = Hanoi(cnt[1],cnt[2])

    return P, Q


def Hanoi(MAX,MIN):
    


    pass
        

N = int(input())
A = []
B = []
C = []
cnt=list(int(input().split()))
for i in range(cnt[0]):
    tem = int(input())
    A[0].append(tem)
for i in range(cnt[1]):
    tem = int(input())
    B[1].append(tem)
for i in range(cnt[2]):
    tem = int(input())
    C[2].append(tem)


P,Q = solve(A,B,C,N,cnt)
print(P)
print(Q)