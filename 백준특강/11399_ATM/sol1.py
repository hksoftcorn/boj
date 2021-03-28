N = int(input())
P = list(map(int, input().split()))

result = []
ans = 0
for _ in range(N):
    min_p = min(P)
    result.append(min_p)
    ans += sum(result)
    P.pop(P.index(min_p))
print(ans)