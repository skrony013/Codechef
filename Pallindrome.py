n = int(input())

org = n
rev = 0

while n != 0:
    rem = n % 10
    print(rem)
    rev = (rev * 10) + rem
    n /= 10
if org == rev:
    print("P")
else:
    print("N")