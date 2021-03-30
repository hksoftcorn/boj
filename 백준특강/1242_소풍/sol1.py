N, K, M = map(int, input().split())

cnt = 0
numbers = list(range(1, N+1))
index = 0

while 1:
    index += K
    index %= len(numbers)

    number = numbers.pop(index)

    if number == M-1:
        break

print(cnt)


