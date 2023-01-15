T = int(input())
for t in range(T):
    def Result(X, Y, Z):
        if X == Y + Z or Y == Z + X or Z == X + Y:
            print("YES")
        else:
            print("NO")


    p, q, r = map(int, input().split())
    Result(p, q, r)
