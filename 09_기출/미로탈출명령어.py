import sys

sys.setrecursionlimit(10 ** 6)

# d l r u 순으로 탐색
dy = [1, 0, 0, -1]
dx = [0, -1, 1, 0]
ch = ['d', 'l', 'r', 'u']
answer = ""

    
def dfs(y, x, r, c, s, k, n, m):
    global answer
    
    if answer != "":
        return 
    
    # 종료 조건
    if len(s) == k:
        if y == r and x == c:
            answer = s
        return
    
    if y == r and x == c and (k - len(s)) % 2 == 1:
        return
    
    expect_dist = len(s) + getDist(y, x, r, c)
    
    if expect_dist > k:
        return
    
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
            
        if ny <= 0 or ny > n or nx <= 0 or nx > m:
            continue
            
        dfs(ny, nx, r, c, s + ch[i], k, n, m)
    
    

def getDist(y, x, yy, xx):
    return abs(yy - y) + abs(xx - x)
    

def solution(n, m, x, y, r, c, k):
    global answer
    
    dist = getDist(y, x, r, c)
    
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    
    dfs(x, y, r, c, "", k, n, m)
    
    if answer == "":
        return "impossible"
        
    return answer
