A, B, C = map(int, input().split())
cost = B - C
if cost >= 0:
    print(-1)
else:
    n = 0
    while A + cost * n >= 0:
        n += 1
    print(n)
