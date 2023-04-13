t = int(input())
for i in range(t):
    N, X = map(int, input().split())
    A = list(map(int, input().strip().split(' ')))[:N]
    flag = 0
    for item in A:
        if item >= X:
            flag = flag + 1
    print(flag)
