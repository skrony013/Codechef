t = int(input())
for i in range(t):
    S = input()
    flag = 0
    for a in range(0, len(S)):
        if S[a] == 'a' or S[a] == 'e' or S[a] == 'i' or S[a] == 'o' or S[a] == 'u':
            if S[a + 1] == 'a' or S[a + 1] == 'e' or S[a + 1] == 'i' or S[a + 1] == 'o' or S[a + 1] == 'u':
                if S[a + 2] == 'a' or S[a + 2] == 'e' or S[a + 2] == 'i' or S[a + 2] == 'o' or S[a + 2] == 'u':
                    flag = 1
                    break

    if flag == 1:
        print("Happy")
    else:
        print("Sad")
