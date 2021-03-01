def solution(str):
    result = ""
    if str == "":
        return ""
    u, v = substring(str)
    if isvalid(u):
        result += u
        result += solution(v)
    else:
        result += '(' + solution(v) + ')'
        for ch in u[1:-1]:
            if ch == '(':
                result += ')'
            else:
                result += '('
    return result



def isvalid(str):
    cnt = 0

    for s in str:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False

    if cnt == 0:
        return True
    else:
        return False


def substring(str):
    cnt = 0

    for i in range(2, len(str)+1):
        if isbalanced(str[:i]) and isbalanced(str[i:]):
            return str[:i], str[i:]


def isbalanced(str):
    cnt = 0

    for s in str:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False
