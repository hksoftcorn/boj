N = int(input())

# sol1
result = 1
if N == 0:
    print(result)
else:
    for n in range(1, N + 1):
        result *= n
    print(result)