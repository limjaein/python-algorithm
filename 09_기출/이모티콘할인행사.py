from itertools import product


def solution(users, emoticons):
    answer = [0, 0] # 플러스서비스 가입자, 판매액
    percents = [10, 20, 30, 40]
    
    for percent in list(product(percents, repeat=len(emoticons))): # 이모티콘 할인율 중복순열
        plus_cnt = 0 # 이모티콘 플러스 서비스 가입자 카운트
        sale_amt_sum = 0 # 판매액 합계
        
        for user_p, user_m in users:
            sale_amt = 0
            
            for i, price in enumerate(emoticons):
                if percent[i] >= user_p: # 사용자가 구매할 수 있는 할인율의 이모티콘인 경우
                    sale_amt += price * (100 - percent[i]) / 100
            
            if sale_amt >= user_m: # 이모티콘 플러스 서비스 가입 조건
                plus_cnt += 1
                sale_amt = 0
            
            sale_amt_sum += sale_amt
            
        if plus_cnt > answer[0]:
            answer = [plus_cnt, sale_amt_sum]
        elif plus_cnt == answer[0]:
            answer[1] = max(answer[1], sale_amt_sum)
            
    
    return answer
