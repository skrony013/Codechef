def isReady(N):
    listA = list(map(int, input().strip().split(' ')))[:N]
    count_of_lucky = 0
    count_of_unlucky = 0
    for item in listA:
        if item % 2 == 0:
            count_of_lucky = count_of_lucky + 1
        else:
            count_of_unlucky = count_of_unlucky + 1
    if count_of_lucky > count_of_unlucky:
        print("READY FOR BATTLE")
    else:
        print("NOT READY")


A = int(input())
isReady(A)
