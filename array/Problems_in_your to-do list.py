T = int(input())
for t in range(T):
    def Remove(N):
        listA = list(map(int, input().strip().split(' ')))[:N]
        cnt = 0
        for num in listA:
            if num >= 1000:
                cnt = cnt + 1
        print(cnt)


    X = int(input())
    Remove(X)
