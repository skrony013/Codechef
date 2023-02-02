t = int(input())
for i in range(t):
    N, X, Y = map(int, input().split())
    if X * Y >= N:
        print("YES")
    else:
        print("NO")
