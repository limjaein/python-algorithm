import sys

def solution():
    meeting_count = int(input())
    meeting_list = list()

    for _ in range(meeting_count):
        s, e = list(map(int, sys.stdin.readline().split()))
        meeting_list.append((s,e))

    meeting_list.sort(key=lambda t:(t[1],t[0]))

    time = 0
    cnt = 0
    for (start, end) in meeting_list:
        if time <= start:
            time = end
            cnt += 1

    print(cnt)

solution()