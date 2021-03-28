A = int(input())

n = 1
while 1:
    y = 3 * n * n - 3 * n + 1
    if A <= y:
        print(n)
        break
    n += 1

