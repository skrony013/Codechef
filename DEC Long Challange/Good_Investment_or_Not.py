T = int(input())
for t in range(T):
    def Investment(X, Y):
        if X >= 2 * Y:
            print("Yes")
        else:
            print("No")


    N, M = map(int, input().split())
    Investment(N, M)
