def solution(list):
    result = 0
    cnt = 0
    goal = 0

    list.sort()

    for num in list:
        cnt += 1

        if goal == 0:
            goal = num
        else:
            if goal < num:
                goal = num
        if cnt == goal:
            result += 1
            cnt = 0
            goal = 0

    return result


print(solution([2, 3, 2, 2, 1]))