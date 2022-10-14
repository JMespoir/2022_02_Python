
def solve(n,low,high):
    if(low > high):
        return -1
    else:
        mid = (low+high) // 2
        if(F[mid] == n):
            return mid
        elif(F[mid] > n):
            return solve(n,low,mid-1)
        else:
            return solve(n,mid+1, high)

F = list()
F.append(0)
F.append(1)
F.append(1)
for i in range(3,50001):
    F.append(F[i-1] + F[i-2])

T = int(input())
for i in range(T):
    num = int(input())
    print(solve(num,1,50000))

        