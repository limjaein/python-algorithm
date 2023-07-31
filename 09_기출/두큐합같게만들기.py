def solution(queue1, queue2):
    total_queue = queue1 + queue2
    
    target = sum(total_queue) // 2
    
    l = 0
    r = len(queue1) - 1
    s = sum(queue1)
    cnt = 0
    
    while True:
        if s < target:
            # 타겟보다 합이 작은데, 더 이동할 수 없을 때
            if r == len(total_queue) - 1:
                return -1
            else:
                r += 1
                s += total_queue[r]
        elif s == target:
            return cnt
        else:
            if l <= r:
                s -= total_queue[l]
                l += 1
            
        cnt += 1
    
    
    return cnt
