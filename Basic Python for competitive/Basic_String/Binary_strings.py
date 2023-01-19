t = int(input())
for i in range(t):
    A = str(input())
    B = str(input())
    a_1_count = 0
    b_1_count = 0
    match_count = 0
    for j in A:
        if j == '1':
            a_1_count = a_1_count + 1
    for k in B:
        if k == '1':
            b_1_count = b_1_count + 1
    for m in range(0, len(A)):
        if A[m] == B[m]:
            match_count = match_count + 1
    print(a_1_count, b_1_count, match_count)
