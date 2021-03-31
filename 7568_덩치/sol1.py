import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

body = []
idx = 0
for _ in range(N):
    weight, height = map(int, input().split())
    body.append((weight, height, idx))
    idx += 1

body.sort(key=lambda x: x[0], reverse=True)

result = {body[0][2]: 1}

rank = 2
for i in range(1, len(body)):
    # 1번 이후 사람과 비교
    if body[i-1][0] > body[i][0] and body[i-1][1] > body[i][1]:
        result[body[i][2]] = rank
    else:
        result[body[i][2]] = result[body[i-1][2]]
    rank += 1

print(' '.join(map(str, [result[i] for i in range(N)])))
