T = int(input())
for t in range(T):
    def CountingProblem(n):
        if n >= 2:
            listA = list(map(int, input().strip().split(' ')))[:n]
            S1 = listA[1::2]
            r1 = sum(S1)
            S2 = listA[0::2]
            r2 = sum(S2)
            if (r1 * r2) % 2 != 0:
                print("YES")
            else:
                print("NO")


    X = int(input())
    CountingProblem(X)