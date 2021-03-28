T = int(input())

for tc in range(T):
    S, R = input().split()
    P = ''
    for r in R:
        P += r * (int(S))
    print(P)
