from itertools import combinations

n,m = input().split(" ")
weight = input().split(" ")

comb_list = list(map(''.join, combinations(weight, 2)))
result = 0

for comb in comb_list:
    num = int(comb)
    if num % 11 != 0 and num % 10 != 0:
        result += 1

print(result)