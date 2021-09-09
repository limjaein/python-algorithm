n = int(input())
ipt = list(map(int, input().split()))
x = int(input())
answer = 0

start = 0
end = len(ipt) - 1

ipt.sort()

while end < len(ipt) and start < len(ipt) - 1:
    if start == end:
        break

    if ipt[start] + ipt[end] == x:
        end -= 1
        answer += 1
    elif ipt[start] + ipt[end] > x:
        end -= 1
    else:
        start += 1

print(answer)

