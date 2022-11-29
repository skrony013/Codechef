T = int(input())
for i in range(0, T):
    l = list(map(int, input().split()))
    l.sort()
    print(l[-2])

