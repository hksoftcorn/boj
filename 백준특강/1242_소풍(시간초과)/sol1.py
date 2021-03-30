import sys
sys.stdin = open('input.txt', 'r')


N, K, M = map(int, input().split())

cnt = 0
numbers = list(range(1, N+1))
index = 0

while 1:
    cnt += 1
    if len(numbers) == 1:
        break

    index += K - 1
    index %= len(numbers)

    number = numbers.pop(index)

    if number == M:
        break

print(cnt)