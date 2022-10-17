#6615: Collatz
def CollatzN(N):
    if N == 1:
        return [1]
    elif N % 2 == 0 :
        return [N] + CollatzN(N//2)
    else:
        return[N] + CollatzN(3*N +1)

def solve(a,b ):
    A = CollatzN(a)
    B = CollatzN(b)
    cnt = 0
    for i in range(len(A)):
        cnt_b = B.count(A[i])
        if(cnt_b >=1):
            cnt_b = B.index(A[i])
            cnt = i
            break
    

    return [cnt, cnt_b, A[cnt]]


while(True):
    A,B = map(int,input().split())
    if(A ==0 and B ==0):
        break
    C = solve(A,B)
    print("{} needs {} steps, {} needs {} steps, they meet at {}".format(A,C[0], B, C[1],C[2]))
