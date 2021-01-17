str = input()

count_zero = 0
count_one = 0
num = -1
next = 0

for i in range(0, len(str)):
    next = int(str[i])
    if num != next:
        if next == 0:
            count_zero += 1
        else:
            count_one += 1
    num = next

print(min(count_zero, count_one))