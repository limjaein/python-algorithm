def solution(array, commands):
    answer = []
    lists = []

    for cmd in commands:
        lists = array[cmd[0] - 1:cmd[1]]
        lists.sort()
        answer.append(lists[cmd[2] - 1])

    return answer