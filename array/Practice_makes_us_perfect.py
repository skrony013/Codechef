li = []


def Count(a, b, c, d):
    li.append(a)
    li.append(b)
    li.append(c)
    li.append(d)
    cnt = 0
    for num in li:
        if num >= 10:
            cnt = cnt + 1
    print(cnt)


P1, P2, P3, P4 = map(int, input().split())
Count(P1, P2, P3, P4)
