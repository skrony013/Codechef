T = int(input())
for t in range(T):
    def Rain(N):
        if N < 3:
            print("LIGHT")
        elif 3 <= N < 7:
            print("MODERATE")
        else:
            print("HEAVY ")


    A = int(input())
    Rain(A)
