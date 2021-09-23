from collections import deque


def solution(k, room_number):
    answer = []
    next_room = {}
    prev_rooms = []

    for number in room_number:
        # 해시로 저장된 이력이 있으면
        if number in next_room:
            while number in next_room:
                prev_rooms.append(number)
                number = next_room.get(number)

            last_number = number + 1
            next_room[number] = last_number
            while prev_rooms:
                prev_room = prev_rooms.pop()
                next_room[prev_room] = last_number
        else:
            next_room[number] = number + 1

        answer.append(number)

    return answer