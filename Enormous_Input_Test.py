def divisible(a, b):
    count = 0
    for i in range(a):
        S = int(input())
        if S % b == 0:
            count += 1
    print(count)


n, k = map(int, input().split())
divisible(n, k)
