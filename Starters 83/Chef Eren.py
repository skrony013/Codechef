t = int(input())
for i in range(t):
    N, A, B = map(int, input().split())
    c1 = 0
    c2 = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            c1 = c1+1
        else:
            c2 = c1+1
    print(c1*A + c2*B)
    # print(c1,c2)
