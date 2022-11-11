#콜라츠 수열의 길이는?
def solve(N):
    max =N
    while(N!=1):
        if(max<N):
            max = N
        if(N%2 == 0):
            N //=2
        else:
            N = N*3 +1
    return max

max = 0
for i in range(12345,54322):
    res = solve(i)
    if(max < res):
        max = res
print(max)