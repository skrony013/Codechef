t = int(input())
for i in range(t):
    A, B, C = map(int, input().split())
    if A * B < 0 or B * C < 0 or C * A < 0:
        print("YES")
    else:
        print("NO")
