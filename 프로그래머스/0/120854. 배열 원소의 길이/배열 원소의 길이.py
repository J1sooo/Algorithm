def solution(strlist):
    answer = []
    for i in strlist:
        c=0
        for j in i:
            c+=1
        answer.append(c)
    return answer