T = int(input())
for t in range(T):
    def Result(x):
        if x < 4:
            print("MILD")
        elif 4 <= x < 7:
            print("MEDIUM")
        else:
            print("HOT")


    A = int(input())
    Result(A)
