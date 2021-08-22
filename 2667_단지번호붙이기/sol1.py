N = int(input())

arr = [0] * (N + 2)
for i in range(N + 2):
    arr[i] = [0] + list(input()) + [0]

visited = [[0] * (N + 2) for _ in range(N + 2)]

for row in range(1, N + 1):
    for column in range(N):
        # 1이면서 가보지 않은 곳
        if arr[row][column] == 1 and visited[row][column] == 0:
            dfs(row, column)


def dfs(row, column):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[row][column] = 1
    for i in range(4):
        row += dx[i]
        column += dy[i]
        while 

