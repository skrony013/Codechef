t = int(input())
for i in range(t):
    S = input()
    T = input()
    M = ""
    for j in range(0, len(S)):
        if S[j] == T[j]:
            M = M + 'G'
        else:
            M = M + 'B'
    print(M)
