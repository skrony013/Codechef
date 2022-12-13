import math

T = int(input())
for t in range(T):
    def Height(N):
        r = 8 * N + 1
        r = math.sqrt(r)
        result = math.trunc((r-1)/2)
        print(result)


    X = int(input())
    Height(X)
