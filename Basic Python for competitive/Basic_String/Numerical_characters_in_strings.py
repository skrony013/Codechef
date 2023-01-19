t = int(input())
for i in range(t):
    A = input()
    flag = 0
    for ele in A:
        if ele == '0' or ele == '5':
            flag = 1
            break
    if flag == 1:
        print("Yes")
    else:
        print("No")
