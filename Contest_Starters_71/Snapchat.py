T = int(input())
for t in range(T):
    def Result(N):
        A = list(map(int, input().strip().split(' ')))[:N]

        B = list(map(int, input().strip().split(' ')))[:N]
        c = 0
        for f, b in zip(A, B):
            if f == 0 or b == 0:
                continue
            else:
                c += 1
        print(c)


    p = int(input())
    Result(p)
