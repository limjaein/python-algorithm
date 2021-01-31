def solution(s):
    length = len(s)
    answer = length
    repeat = ""

    for l in range(1, int(length/2)+1):
        cnt = 0
        new_length = 0
        idx = 0

        while True:
            if cnt != 0:
                if s[idx:idx + l] == repeat:
                    cnt += 1
                else:
                    if cnt != 1:
                        new_length += len(str(cnt))
                    cnt = 0

            if idx + l >= length:
                if cnt == 0:
                    new_length += length - idx
                else:
                    new_length += len(str(cnt))
                break

            if cnt == 0:
                cnt = 1
                repeat = s[idx:idx+l]
                new_length += l

            idx += l

        answer = min(answer, new_length)

    return(answer)