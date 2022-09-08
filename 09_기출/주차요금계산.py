import math


def solution(fees, records):
    answer = []
    in_time = dict()
    parking_time = dict()
    car_fee = []

    # record 조회하며 IN 이면 dict 에 저장 OUT 이면 주차시간 누적 및 dict 제거
    for record in records:
        time, car_no, type = record.split(" ")
        hour, min = map(int, time.split(":"))
        if type == "IN":
            in_time[car_no] = (hour, min)
        else:
            in_hour, in_min = in_time[car_no]
            diff = getDiffTime(in_hour, in_min, hour, min)
            if car_no not in parking_time:
                parking_time[car_no] = diff
            else:
                parking_time[car_no] = parking_time[car_no] + diff
            in_time.pop(car_no)

    # 출차하지 않은경우 23:59분 출차로 간주
    for car_no in in_time:
        in_hour, in_min = in_time[car_no]

        diff = getDiffTime(in_hour, in_min, 23, 59)
        if car_no not in parking_time:
            parking_time[car_no] = diff
        else:
            parking_time[car_no] = parking_time[car_no] + diff

    # 누적 주차 비용 계산
    for car_no in parking_time:
        car_fee.append((car_no, calculateFee(parking_time[car_no], fees)))

    car_fee.sort(key=lambda x:(x[0]))

    # 번호가 작은 차량부터 결과 배열에 담기
    for car, fee in car_fee:
        answer.append(fee)

    return answer


def getDiffTime(in_hour, in_min, out_hour, out_min):
    if in_min > out_min:
        in_hour -= 1
        in_min += 60

    return out_min - in_min + (out_hour - in_hour) * 60


def calculateFee(diff_time, fees):
    fee = fees[1]

    if diff_time <= fees[0]:
        return fee

    return fee + math.ceil((diff_time - fees[0]) / fees[2]) * fees[3]





print(solution( [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN"
    , "23:00 5961 OUT"]))