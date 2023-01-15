T = int(input())
for t in range(T):
    def Result(D,L,R):
        if L <= D <= R:
            print("Take second dose now")
        elif D<L:
            print("Too Early")
        else:
            print("Too Late")


    p, q, r = map(int, input().split())
    Result(p, q, r)
