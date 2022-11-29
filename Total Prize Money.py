T = int(input())
for i in range(1, T + 1):
    X, Y = map(int, input().split())
    r = 10 * X + 90 * Y
    print(r)
