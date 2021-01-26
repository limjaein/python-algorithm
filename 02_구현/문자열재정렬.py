S = list(input())
sum = 0

S.sort()
for i in range(len(S)):
    if S[i] < 'A' or S[i] > 'Z':
        sum += int(S[i])
    else:
        result = ''.join(S[i:]) + str(sum)
        break

print(result)