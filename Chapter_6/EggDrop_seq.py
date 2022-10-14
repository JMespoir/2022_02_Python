#EggDrop sequential
def eggdrop(n, T):
    global cnt
    cnt += 1
    return n >= T # 계란이 깨지면 True, 안 깨지면 False

def solve(N, T):
    for i in range(1, N + 1):
        if eggdrop(i, T):
            return T
    return -1

import random
N = 100
T = random.randint(1, N)
cnt = 0
print(T, solve(N, T), cnt)