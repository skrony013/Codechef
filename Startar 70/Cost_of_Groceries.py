T = int(input())
for t in range(T):
    def Result(n, x):
        A = list(map(int, input().strip().split(' ')))[:n]

        B = list(map(int, input().strip().split(' ')))[:n]

        cost = 0
        for item in range(0, len(A)):
            if A[item] >= x:
                for item2 in range(0, len(B)):
                    if item == item2:
                        cost = cost + B[item2]
        print(cost)


    p, q = map(int, input().split())
    Result(p, q)
