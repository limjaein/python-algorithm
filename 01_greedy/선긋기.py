n = int(input())
lines = []

for _ in range(n):
    l, r = input().split()
    lines.append((int(l), int(r)))

lines.sort()

sum = 0
p_l = -1e9
p_r = -1e9
for (n_l, n_r) in lines:
    if n_l < p_r:
        if p_r >= n_r:
            continue
        else:
            sum += n_r - p_r
            p_r = n_r
    else:
        sum += n_r - n_l
        p_r = n_r
        if n_l > p_r:
            p_l = n_l

print(sum)