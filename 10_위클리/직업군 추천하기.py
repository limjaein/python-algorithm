MAX_JOB_CNT = 5


def solution(table, languages, preference):
    answer = 0
    pref_dict = dict()
    job_dict = {0: "SI", 1: "CONTENTS", 2: "HARDWARE", 3: "PORTAL", 4: "GAME"}
    job_score = [0] * MAX_JOB_CNT  # 직업군 언어점수

    # key:lang, value:pref dict
    for idx, lang in enumerate(languages):
        pref_dict[lang] = preference[idx]

    for j_idx, job_info in enumerate(table):
        langs = job_info.split(" ")
        # 직업군 언어 점수 탐색
        for l_idx, lang in enumerate(langs):
            if l_idx == 0:
                continue
            # 선호 언어가 있다면
            if lang in languages:
                job_score[j_idx] += (6 - l_idx) * pref_dict[lang]

        if job_score[answer] < job_score[j_idx] or (job_score[answer] == job_score[j_idx] and job_dict[j_idx] < job_dict[answer]):
            answer = j_idx

    return job_dict[answer]