T = int(input())
for t in range(T):
    def Result(x, y, z):
        if x == y or y == z or z == x:
            print("NO")
        else:
            print("YES")


    A, B, C = map(int, input().split())
    Result(A, B, C)
