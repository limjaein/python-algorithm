import re


answer = 0
id_int = set()
id_idx = dict()


def findResult(idx, user_id, banned_id, isSelected):
    global answer

    if idx == len(banned_id):
        if isSelected not in id_int:
            answer += 1
            id_int.add(isSelected)
        return

    ids = []
    regex = re.compile(banned_id[idx])

    for id in user_id:
        if len(id) == len(banned_id[idx]) and regex.match(id):
            ids.append(id)

    for id in ids:
        if isSelected & (1 << id_idx[id]) == 0:
            isSelected = isSelected | (1 << id_idx[id])
            findResult(idx + 1, user_id, banned_id, isSelected)
            isSelected = isSelected & ~(1 << id_idx[id])

def solution(user_id, banned_id):
    global answer

    for i in range(len(banned_id)):
        banned_id[i] = str.replace(banned_id[i], '*', '.')

    for i in range(len(user_id)):
        id_idx[user_id[i]] = i

    findResult(0, user_id, banned_id, 0)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	, ["*rodo", "*rodo", "******"]	)
print(answer)