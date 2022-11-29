T = int(input())
for t in range(T):
    def manipulate(a, b):
        if a >= b:
            print("Yes")
        else:
            print("No")


    x, y = map(int, input().split())
    manipulate(x, y)
