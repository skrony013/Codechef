t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    temp = Y
    minute = 0
    while temp < X:
        minute = minute + 1
        temp = temp + minute

    print(minute)
