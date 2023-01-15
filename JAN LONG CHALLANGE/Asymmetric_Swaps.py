t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().strip().split(' ')))[:N]
    B = list(map(int, input().strip().split(' ')))[:N]
    A.extend(B)
    A.sort()

    R = []
    for j in range(0, N + 1):
        x = A[N + j - 1] - A[j]
        R.append(x)
    R.sort()
    print(R[0])
