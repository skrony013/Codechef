T = int(input())
for t in range(T):
    def Output(A, C):
        r2 =0
        r1 = 2 ** C
        for i in range(A):
            r2 = r1 // 2
            r1 = r2
        print(r2)
    N, M = map(int, input().split())
    Output(N, M)
