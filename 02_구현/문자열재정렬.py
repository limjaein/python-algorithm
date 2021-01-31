S = list(input())
S.sort()
sum = 0

for i in range(len(S)):
    if S[i] < 'A' or S[i] > 'Z':
        sum += int(S[i])
    else:
        result = ''.join(S[i:]) + str(sum)
        break

print(result)