t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if (a + b + c) <= 5:
        print("No")
    else:
        print("Yes")
