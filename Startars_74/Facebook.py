t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().strip().split(' ')))[:N]
    B = list(map(int, input().strip().split(' ')))[:N]
    e1 = A[0]
    chk = True
    for m in A:
        if m != e1:
            chk = False
            break
    if chk == True:
        print(B.index(max(B)) + 1)
    else:
        print(A.index(max(A)) + 1)
