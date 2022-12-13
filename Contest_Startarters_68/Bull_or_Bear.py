T = int(input())
for t in range(T):
    def ProfitCalc(a, b):
        if a<b:
            print("PROFIT")
        elif a == b:
            print("NEUTRAL")
        else:
            print("LOSS")

    N, M = map(int, input().split())
    ProfitCalc(N, M)
