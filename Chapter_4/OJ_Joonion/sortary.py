#양의정수정렬하기 자릿수가 작은 수가 먼저나오세요, 자릿수가 같다면 더 큰수가 나오세요
N = int(input())

ary = input().split()

ary.sort(key=lambda x: (len(x),-int(x)))
print(" ".join(map(str,ary)))