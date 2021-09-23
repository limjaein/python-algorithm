from collections import deque


def solution(k, room_number):
    answer = []
    next_room = {}
    prev_rooms = []

    for i in range(1, k + 1):
        next_room[i] = i

    for number in room_number:
        # 다음 방 번호가 자신이 아닐 경우
        while next_room[number] != number:
            prev_rooms.append(number)
            number = next_room[number]

        last_number = number + 1
        next_room[number] = last_number
        while prev_rooms:
            prev_room = prev_rooms.pop()
            next_room[prev_room] = last_number

        answer.append(number)

    return answer
