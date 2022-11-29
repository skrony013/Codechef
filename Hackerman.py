import math

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    r = A + B
    count = 0
    for j in range(2, math.floor(math.sqrt(r)) + 1):
        if r % j == 0:
            print("Bob")
            break
        count += 1

    if count + 2 == math.floor(math.sqrt(r)) + 1:
        print("Alice ")
