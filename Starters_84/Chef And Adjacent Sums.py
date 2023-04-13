t = int(input())
for j in range(t):
    N = int(input())
    A = list(map(int, input().strip().split(' ')))[:N]
    B = sorted(A)
    Z = B[N-1] + B[N - 2]
    rearranged = False
    for i in range(N-1):
        if A[i] + A[i+1] < Z:
            A[i], A[i+1] = A[i+1], A[i]
            rearranged = True
    if rearranged:
        print("YES")
    else:
        print("NO")
