T = int(input())
for t in range(T):
    def minChair(a, b):
        if a>b:
            print(a - b)
        else:
            print(0)


    X, Y = map(int, input().split())
    minChair(X, Y)
