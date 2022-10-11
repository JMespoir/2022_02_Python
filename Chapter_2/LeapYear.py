# 2753 : Leapyear

def solve(year):
    if(year%400 == 0 or (year%4==0 and year%100!=0)):
        return 1
    else:
        return 0


Year = int(input())

print(solve(Year))