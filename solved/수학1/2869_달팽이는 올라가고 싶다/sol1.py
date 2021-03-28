A, B, V = map(int, input().split())

cnt = 1
V -= A
if V <= 0:
    print(cnt)
else:
    q, r = divmod(V, A-B)
    cnt += q
    if r:
        cnt += 1
    print(cnt)