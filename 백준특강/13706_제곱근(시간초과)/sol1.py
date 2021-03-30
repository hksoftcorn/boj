N = int(input())
for num in range(N//2, 0, -1):
    if (num * num) == N:
        print(num)
        break
