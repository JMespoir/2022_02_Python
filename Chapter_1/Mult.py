#2588 : xxx * xxx multiple

N = int(input())
S = int(input())

print(N*(S%10))
print(N*(S//10%10))
print(N*(S//100))
print(N*S)