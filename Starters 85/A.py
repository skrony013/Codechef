# t = int(input())
# for i in range(t):
#     N, M = map(int, input().split())
#     if N <= M:
#         print("0")
#     else:
#         print(N - M)

# t = int(input())
# for i in range(t):
#     X, Y = map(int, input().split())
#     if X*15 >= 2*Y:
#         print("YES")
#     else:
#         print("NO")

# T = int(input())
# for t in range(T):
#     N = int(input())
#     A = list(map(int, input().strip().split(' ')))[:N]
#     cnt = 0
#     b = 1
#     i = 0
#     r = 0
#     for i in range(0, len(A)):
#         r = r + A[i]
#         if r/(i+1) == 1:
#             cnt = cnt+1
#     print(cnt)

T = int(input())
for t in range(T):
    N = int(input())
    ans = 0
    k = 20
    ans = ans * 10 + N % k
    print(ans)
