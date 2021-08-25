# 12:30

spelling_numbers = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5"
                    , "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    for number in spelling_numbers.keys():
        if number in s:
            s = s.replace(number, spelling_numbers[number])
    return int(s)