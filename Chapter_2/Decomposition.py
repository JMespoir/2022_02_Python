# 2231 : Decomposition
def solve(n):
    for i in range(1,1000001):
        sum = 0
        i = str(i)
        if(len(i)==1):
            sum = int(i)*2
        else:
            sum = int(i)
            for j in range(len(i)):
                sum += int(i[j])

        if(sum == n):
            return i
    return 0

N = int(input())
print(solve(N))

    
