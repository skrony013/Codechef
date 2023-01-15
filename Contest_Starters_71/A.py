T = int(input())
for t in range(T):
    def Result(X, Y):
        if Y * 10 >= X:
            print("NO")
        else:
            print("YES")


    p, q = map(int, input().split())
    Result(p, q)
