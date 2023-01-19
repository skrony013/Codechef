t = int(input())
for i in range(t):
    S = input()
    A = []
    for j in S:
        A.append(ord(j))
    print(*A)
