def solution(enter, leave):
    N = len(enter)
    answer = [0] * N
    room = 0
    e_idx = 0
    pair = set()

    for l_num in leave:
        while not room & (1 << l_num):
            if e_idx == len(enter):
                break

            room = room | (1 << enter[e_idx])
            e_idx += 1

        for num in range(1, N + 1):
            if room & (1 << num):
                if num == l_num:
                    continue
                pair.add((min(num, l_num), max(num, l_num)))

        room = room & ~(1 << l_num)

    for p in pair:
        answer[p[0] - 1] += 1
        answer[p[1] - 1] += 1

    return answer


print(solution(	[1, 3, 2], [1, 2, 3]))