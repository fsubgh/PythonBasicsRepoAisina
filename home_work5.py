n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

transposed = [[0] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        transposed[j][i] = matrix[i][j]

for row in transposed:
    print(*row)