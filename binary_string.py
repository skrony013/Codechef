T = int(input())
for t in range(T):
    def Result(D,L,R):
        if L <= D <= R:
            print("Take second dose now")
        elif D<L:
            print("Too Early")
        else:
            print("Too Late")


    p = int(input())
    Result(p)
