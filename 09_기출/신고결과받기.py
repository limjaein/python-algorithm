def solution(id_list, report, k):
    bad_user = dict()
    answer = [0] * len(id_list)

    # 불량 유저를 신고한 신고 유저리스트 저장
    for ids in report:
        a, b = ids.split(" ")
        if b in bad_user:
            mail_user_list = bad_user[b]
            if a not in mail_user_list:
                mail_user_list.append(a)
                bad_user[b] = mail_user_list
        else:
            bad_user[b] = [a]

    # 불량 유저를 신고한 유저가 k명 이상일때 신고 유저의 메일 카운트 + 1
    for id in id_list:
        if id in bad_user and len(bad_user[id]) >= k:
            for idx, mail_user in enumerate(id_list):
                if mail_user in bad_user[id]:
                    answer[idx] += 1

    return answer