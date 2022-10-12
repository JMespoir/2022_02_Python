# 1977 : perfect Square Number
def solve(m,n):
    count = 0
    min = 0
    sum = 0
    for i in range(m,n+1):
        if(int(i**0.5) *int(i**0.5)==i ):
            if(count==0):
                min = i
                count += 1
            sum += i

    if(count == 0):
        print(-1)
    else:
        print("{}\n{}".format(sum,min))

M = int(input())
N = int(input())

solve(M,N)