N = 5
M = 8
K = 3
numbers = [2,4,5,4,6]
lists = numbers
result = 0

first = lists[0]
second = lists[1]

count = (M // (K + 1)) * K
count += M % (K + 1)

result = first * count
result += second * (M - count)

print(result)