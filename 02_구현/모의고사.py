def solution(answers):
    answer = []
    scores = [0, 0, 0]
    no1 = [1, 2, 3, 4, 5]
    no2 = [2, 1, 2, 3, 2, 4, 2, 5]
    no3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # range(a,b)는 a부터 b-1까지 반복한
    for i in range(0, len(answers)):
        # python은 증감연산자를 사용할 수 없다
        if answers[i] == no1[i % len(no1)]:
            scores[0] += 1
        if answers[i] == no2[i % len(no2)]:
            scores[1] += 1
        if answers[i] == no3[i % len(no3)]:
            scores[2] += 1

    for i in range(0, 3):
        if scores[i] == max(scores):
            answer.append(i + 1)

    answer.sort()

    return answer