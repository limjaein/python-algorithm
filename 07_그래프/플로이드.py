
n = int(input())
m = int(input())
busCharge = [[100] * n for _ in range(n)]

for i in range(m):
    a, b, c = list(map(int, input().split()))
    busCharge[a-1][b-1] = min(busCharge[a-1][b-1], c)

for i in range(n):
    busCharge[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            busCharge[i][j] = min(busCharge[i][j], busCharge[i][k] + busCharge[k][j])

for i in range(n):
    row = ""
    for j in range(n):
        row += str(busCharge[i][j]) + " "
    

