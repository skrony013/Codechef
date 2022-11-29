import math

T = int(input())
for t in range(T):
    def binaryBattle(x, y, z):
        if x >= 2:
            n = math.log2(x)
            r = n * y + (n - 1) * z
            print(math.trunc(r))
    N, A, B = map(int, input().split())
    binaryBattle(N, A, B)
