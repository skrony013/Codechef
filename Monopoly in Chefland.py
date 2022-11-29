T = int(input())
for i in range(T):
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] > l[0] + l[1]:
        print("Yes")
    else:
        print("No")
