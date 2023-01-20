t = int(input())
for i in range(t):
    N = int(input())
    S = input()
    c = 0
    for i in range(0,N-1):
        if S[i] == S[i+1]:
            c = c+1
    print(c)