from math import trunc

T = int(input())
for t in range(T):
    def ProfitCalc(A, C):
        r = A + C
        if r % 2 == 0:
            B = r / 2
            if C - B == B - A:
                r1 = trunc(B)
                print(r1)
            else:
                print(-1)
        else:
            print(-1)


    N, M = map(int, input().split())
    ProfitCalc(N, M)
