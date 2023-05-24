def getLastDay(day, add_m):
    y = int(day[:4])
    m = int(day[4:6])
    d = int(day[6:8])
    
    # 일 계산
    if d == 1:
        m = m - 1
        d = 28
    else:
        d -= 1
    
    # 달 계산
    m += add_m
    
    if m > 12:
        if m % 12 == 0:
            y += int(m / 12) - 1
            m = 12
        else:
            y += int(m / 12)
            m = m % 12
    
    print(str(y) + ("0" + str(m))[-2:] + ("0" + str(d))[-2:])
    
    return str(y) + ("0" + str(m))[-2:] + ("0" + str(d))[-2:]


def solution(today, terms, privacies):
    answer = []
    exp_types = dict()
    
    for term in terms:
        type, m = term.split(" ")
        exp_types[type] = int(m)
    
    for i, privacy in enumerate(privacies):
        collect_day, type = privacy.split(" ")
        collect_day = collect_day.replace(".", "")
        
        # 유효기간이 지난경우
        if today.replace(".", "") > getLastDay(collect_day, exp_types[type]):
            answer.append(i + 1)
        
    return answer
