import math

t = int(input())
for i in range(t):
    A, B, C, D = map(int, input().split())
    r1 = math.sqrt(pow(A, 2) + pow(B, 2))
    r2 = math.sqrt(pow(C, 2) + pow(D, 2))
    if r1 > r2:
        print("ALEX")
    elif r1 == r2:
        print("EQUAL")
    else:
        print("BOB")
