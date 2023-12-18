def solution(s):
    s = sorted(s)
    result = ''
    for x in range (len(s)):
        if s.count(s[x]) == 1:
            result += s[x]
            
    return result 
    