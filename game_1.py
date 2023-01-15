t = int(input())

for i in range(t):
    x, y = map(int, input().split())

    d = abs(y - x)
    print(d)
