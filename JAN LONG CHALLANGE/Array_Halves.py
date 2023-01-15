t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().strip().split(' ')))[:2 * N]
    R = []
    V = []
    for j in range(N):
        if A[j]>N:
            R.append(j)

    for k in range(N, 2 * N):
        if A[k] <=N:
            V.append(k)

    for l in range(len(R)-1,1):
        pass

