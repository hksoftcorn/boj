N = int(input())

for i in range(N//5, -1, -1):
    b = N - 5 * i
    if b % 3 == 0:
        print(i + b//3)
        break
else:
    print(-1)