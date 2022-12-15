T = int(input())
for t in range(T):
    def DrawOrNot(x, y, z):
        if x == y + z or y == x + z or z == x + y:
            print("Yes")
        else:
            print("No")


    A, B, C = map(int, input().split())
    DrawOrNot(A, B, C)
