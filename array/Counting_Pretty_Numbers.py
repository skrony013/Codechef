T = int(input())
for t in range(T):
    def PrettyNumber(L, R):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for num in range(L, R+1):
            if num % 10 == 2:
                cnt1 = cnt1 + 1
            if num % 10 == 3:
                cnt2 = cnt2 + 1
            if num % 10 == 9:
                cnt3 = cnt3 + 1

        print(cnt1+cnt2+cnt3)


    a, b = map(int, input().split())
    PrettyNumber(a, b)
