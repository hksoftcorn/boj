import sys
sys.stdin = open('input.txt')


A, B = map(int, input().split())


def solution(A, B):
    cnt = 1

    while 1:
        if A > B:
            return -1

        if B % 2 == 0:
            B //= 2
            cnt += 1

        else:
            tmp = str(B)
            B = int(tmp[:-1])
            cnt += 1

        if B == A:
            return cnt

print(solution(A, B))