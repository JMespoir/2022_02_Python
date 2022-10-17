#6615 : Collatz prof code
def solve(A,B):
    a = collatz(A)[::-1]
    b = collatz(B)[::-1]
    minlen = min(len(a),len(b))
    i = 0
    while True:
        if i == minlen or a[i] != b[i]:
            break
        i += 1
    return len(a) - i, len(b) - i, a[i-1]

def collatz(N):
    if N == 1:
        return [1]
    elif N % 2 == 0 :
        return [N] + collatz(N//2)
    else:
        return[N] + collatz(3*N +1)


while True:
    A,B = map(int,input().split())
    if A == 0 and B ==0:
        break
    a1, a2, a3 = solve(A,B)
    print(f"{A} needs {a1} steps, {B} needs {a2} steps, they meet at {a3}")
