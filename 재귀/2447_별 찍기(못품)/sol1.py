import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [['*'] * N for _ in range(N)]

k = 0
while 1:
    k += 1
    N //= 3
    if N == 1:
        break

# 1 <= k < 8
# f(1) + f(1) + f(1)
# f(1) + 000 + f(1)
# f(1) + f(1) + f(1)
print(arr)

