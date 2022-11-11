#스무고개 놀이의 횟수
def solve(N,M,cnt,ary):
    count = 0
    for i in range(cnt):
        tem_cnt = 1
        low = N
        high = M
        while(high>=low):
            mid = (high+low)//2
            if(mid==ary[i]):
                count += tem_cnt
                break
            elif(mid>ary[i]):
                high = mid-1
                tem_cnt +=1
            else:
                low = mid+1
                tem_cnt +=1

    return count


N,M = map(int,input().split())
count = int(input())
ary = list(map(int,input().split()))
print(solve(N,M,count,ary))