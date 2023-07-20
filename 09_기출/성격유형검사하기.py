def solution(survey, choices):
    answer = ''
    
    alps = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    alp_idx = {'R':0, 'T':1, 'C':2, 'F':3, 'J':4, 'M':5, 'A':6, 'N':7}
    scores = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i, str in enumerate(survey):
        # 1, 2, 3점으로 점수 환산
        score = choices[i] - 4
        
        # 0보다 작은 경우 비동의 케이스이므로, 첫번째 캐릭터에서 그만큼 빼준다
        if score < 0:
            scores[alp_idx[str[0]]] -= score
        else:
            scores[alp_idx[str[1]]] += score
    
    for i in range(4):
        if scores[i*2] >= scores[i*2+1]:
            answer += alps[i*2]
        else:
            answer += alps[i*2+1]
    
    return answer

