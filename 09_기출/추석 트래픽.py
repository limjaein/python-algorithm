from decimal import Decimal


class Timestamp:
    def __init__(self, h, m, s, type):
        self.hour = h
        self.minute = m
        self.second = s
        self.type = type

    def __lt__(self, other):
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute < other.minute:
                return True
            elif self.minute == other.minute:
                if self.second < other.second:
                    return True
                elif self.second == other.second:
                    if self.type > other.type:
                        return True
        return False


def getStartTime(end_time, during, type):
    if during < 0:
        second = end_time.hour * 60 * 60 + end_time.minute * 60 + Decimal(str(end_time.second)) - Decimal(
            str(-during)) + Decimal("0.001")
    else:
        second = end_time.hour * 60 * 60 + end_time.minute * 60 + Decimal(str(end_time.second)) + Decimal(
            str(during)) - Decimal("0.001")

    h = int(second / (60 * 60))
    m = int((second - h * 60 * 60) / 60)
    s = second - h * 60 * 60 - m * 60

    return Timestamp(h, m, s, type)


def solution(lines):
    # 초당 최대 처리량
    answer = 0
    timestamps = []

    for line in lines:
        date, time, during = line.split(" ")
        hour, minute, second = time.split(":")
        end_time = Timestamp(int(hour), int(minute), float(second), "")
        timestamps.append(getStartTime(end_time, -float(during[:-1]), "START"))
        timestamps.append(getStartTime(end_time, 1.0, "END"))

    timestamps.sort()

    tmp_answer = 0
    for stamp in timestamps:
        if stamp.type == "START":
            tmp_answer += 1
            answer = max(answer, tmp_answer)
        else:
            tmp_answer -= 1

    return answer