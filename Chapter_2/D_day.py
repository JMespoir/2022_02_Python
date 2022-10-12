#D-day caculator + 윤날 = 366일
def solve(T,D):
    day = 0
    YEAR,MONTH,DAY = 0,1,2
    if(T[YEAR]+1000 == D[YEAR]):
        if(T[MONTH]==D[MONTH] and T[DAY]<=D[DAY]):
            return print("gg")
        if(T[MONTH]<D[MONTH] ):
            return print("gg")
    elif(T[YEAR]+1000<D[YEAR]):
        return print("gg")

    if(T[YEAR]==D[YEAR]):
        month = year(T[YEAR])
        for i in range(T[MONTH],D[MONTH]):
            day += month[i]
        day += D[DAY]-T[DAY]
    else:
        month = year(T[YEAR])
        for i in range(T[MONTH],13):
            day += month[i]
        day -= (T[DAY])

        for i in range(T[YEAR]+1,D[YEAR]):
            if i % 400 == 0 or (i%4==0 and i % 100 != 0):
                day += 366
            else:
                day += 365
        
        month = year(D[YEAR])
        for i in range(1,D[MONTH]):
            day += month[i]
        day += D[DAY]
    return print("D-{}".format(day))

        
def year(year):
    if year % 400 == 0 or (year%4==0 and year % 100 != 0):
        month=[-1,31, 29, 31, 30, 31, 30, 31, 31, 30, 31,30, 31 ]
        return month
    else:
        month=[-1,31, 28, 31, 30, 31, 30, 31, 31, 30, 31,30, 31 ]
        return month

Today = list(map(int,input().split()))
Dday = list(map(int,input().split()))
solve(Today,Dday)