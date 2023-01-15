from math import trunc

T = int(input())
for t in range(T):
    def Result(A, B, X):
        r1 = (B - A) / X
        print(trunc(r1))


    p, q, r = map(int, input().split())
    Result(p, q, r)
