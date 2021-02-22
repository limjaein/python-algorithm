# 0 기둥 1 보
# 0 삭제 1 설치

things = set()


def solution(n, build_frame):
    global things
    answer = []

    for frame in build_frame:
        if isvalid(frame[0], frame[1], frame[2], frame[3]):
            if frame[3] == 0:  # 삭제
                things.remove((frame[0], frame[1], frame[2]))
            else:  # 설치
                things.add((frame[0], frame[1], frame[2]))

    for thing in sorted(things):
        answer.append(list(thing))

    return answer


def isvalid(x, y, frame, action):
    result = True
    if frame == 0:  # 기둥
        if action == 0:  # 삭제
            # 위에 기둥이 있는 경우, 닿아 있는 보가 없으면
            if (x, y + 1, 0) in things and (x - 1, y + 1, 1) not in things and (x, y + 1, 1) not in things:
                result = False
            else:  # 위에 보가 있는 경우, 3개가 연달아 있지 않고 아래에 기둥도 없으면
                if (((x - 1, y + 1, 1) in things and not checkThreeBos(x - 1, y + 1) and (x - 1, y, 0) not in things) or
                        ((x, y + 1, 1) in things and not checkThreeBos(x, y + 1) and (x + 1, y, 0) not in things)):
                    result = False
        else:  # 설치
            # 바닥위거나 보 한쪽끝 위에 있거나 기둥 위인 경우
            if y == 0 or (x - 1, y, 1) in things or (x, y, 1) in things or (x, y - 1, 0) in things:
                pass
            else:
                result = False
    else:  # 보
        if action == 0:  # 삭제
            # 각 끝에 기둥이 있는 경우
            if (((x, y, 0) in things and (x - 1, y, 1) not in things and (x, y - 1, 0) not in things)
                    or ((x + 1, y, 0) in things and (x + 1, y, 1) not in things and (x + 1, y - 1, 0) not in things)):
                result = False
            # 양쪽 끝이 연결된 보에 영향을 주는 경우
            if (((x - 1, y, 1) in things and (x - 2, y, 1) in things and (x, y - 1, 0) not in things and (
                    x - 1, y - 1, 0) not in things)
                    or ((x + 1, y, 1) in things and (x + 2, y, 1) in things and (x + 1, y - 1, 0) not in things and (
                            x + 2, y - 1, 0) not in things)):
                result = False
        else:  # 설치
            # 한쪽 끝이 기둥위에 있거나, 양쪽 끝이 다른 보로 연결된 게 있다면
            if ((x, y - 1, 0) in things or (x + 1, y - 1, 0) in things
                    or ((x - 1, y, 1) in things and (x + 1, y, 1) in things)):
                pass
            else:
                result = False
    return result


def checkThreeBos(x, y):
    if (x - 1, y, 1) in things and (x + 1, y, 1) in things:
        return True
    else:
        return False