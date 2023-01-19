# t = int(input())
# for i in range(t):
#     A = input()
#     B = input()
#     A1 = ""
#     for j in A:
#         A1 = j + A1
#     if A1 == B:
#         print("Yes")
#     else:
#         print("No")

t = int(input())
for i in range(t):
    A = input()
    B = input()
    A1 = ""
    n = len(A)
    flag = 1
    for j in range(0, n):
        if A[j] == B[n - j - 1]:
            pass
        else:
            flag = 0
            break
    if flag == 0:
        print("No")
    else:
        print("Yes")
