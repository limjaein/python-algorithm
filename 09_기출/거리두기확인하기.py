
MAX_SIZE = 5


def getDist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


def isValidDist(y1, x1, y2, x2, place):
    dist = getDist(y1, x1, y2, x2)

    if dist <= 2:
        # 자리 사이에 파티션이 있는 경우 허용
        if dist == 2:
            # 같은 열일 경우
            if y1 == y2 and place[y1][int((x1 + x2) / 2)] == "X":
                return True
            elif x1 == x2 and place[int((y1 + y2) / 2)][x1] == "X":
                return True
            elif place[y1][x2] == "X" and place[y2][x1] == "X":
                return True
        return False
    else:
        return True


def solution(places):
    answer = []

    for place in places:
        participants = []

        for col in range(MAX_SIZE):
            for row in range(MAX_SIZE):
                if place[col][row] == 'P':
                    participants.append((col, row))

        isAllValidDist = True
        for i in range(len(participants)):
            for j in range(i + 1, len(participants)):
                if not isValidDist(participants[i][0], participants[i][1]
                                    , participants[j][0], participants[j][1], place):
                    isAllValidDist = False
                    break
            if not isAllValidDist:
                break

        if isAllValidDist:
            answer.append(1)
        else:
            answer.append(0)

    return answer