# SpotNumber
def solve(l,s):
    high,low = s, 0
    while(high>=low):
        mid = (high+low) // 2
        if(l[mid] == mid):
            return mid
        elif(l[mid]<mid):
            low = mid+1
        else:
            high = mid -1
    return -1

S = int(input())
L = list(int(input())for _ in range(S))
print(solve(L,S))
