T = int(input())
for t in range(T):
    def isAllow(a, b):
        if ((a * 107) / 100) >= b:
            print("Yes")
        else:
            print("No")


    X, Y = map(int, input().split())
    isAllow(X, Y)

