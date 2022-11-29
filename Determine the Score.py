import math
T = int(input())
for t in range(T):
    def detScore(a, b):
        r = (a / 10) * b
        print(math.trunc(r))


    X, N = map(int, input().split())

    detScore(X, N)
