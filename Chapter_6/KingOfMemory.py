#2776 : King Of Memorization
import sys
input = sys.stdin.readline

def binsearch(A,el):
    high, low = len(A)-1, 0
    while(high>=low):
        mid = (high + low) //2
        if(A[mid]== el):
            return 1
        elif(A[mid] > el):
            high = mid-1
        else:
            low = mid+1
    return 0

def solve(A,B,num):
    for i in range(num):
        print(binsearch(A,B[i]))


T = int(input())
for i in range(T):
    NUMA = int(input())
    A = list(map(int,input().split()))
    A.sort()

    NUMB = int(input())
    B= list(map(int,input().split()))
    solve(A,B,NUMB)