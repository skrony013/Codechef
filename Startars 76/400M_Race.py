T = int(input())
for i in range(T):
    X, Y, Z = map(int, input().split())
    if X < Y and X < Z:
        print("ALICE")
    elif Y < X and Y < Z:
        print("BOB")
    else:
        print("CHARLIE")