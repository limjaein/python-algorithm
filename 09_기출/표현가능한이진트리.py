def check(n):
    l = len(n)
    
    if l == 1 or '1' not in n or '0' not in n:
        return True
    
    mid = l//2
    if n[mid] == "0":
        return False
    
    return check(n[:mid]) and check(n[mid+1:])


def solution(numbers):
    answer = []
    
    for number in numbers:
        n = bin(number)[2:]
    
        # 2^n - 1 개수 맞추기
        for i in range(51):
            if 2**i - 1 >= len(n):
                n = "0" * (2**i - 1 - len(n)) + n
                break
        
        answer.append(1 if check(n) else 0)
        
    return answer
