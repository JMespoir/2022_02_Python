#이 프로젝트는 X년 1월 1일에 시작해서 Y년 12월 31일에 종료한다고 한다.

def solve(N,M):
    res = 0
    for i in range(N,M+1):
        if(isYear(i)):
            res += 366
        else:
            res += 365
    return res

def isYear(year):
    if year %400 == 0 or (year%4==0 and year %100 != 0):
        return True
    return False

X = int(input())
Y = int(input())
print(solve(X,Y))