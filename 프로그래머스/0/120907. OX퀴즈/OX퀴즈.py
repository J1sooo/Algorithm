def solution(quiz):
    answer = []
    for i in quiz:
        a,b,c,d,e=i.split()
        a,c,e=int(a),int(c),int(e)
        if b=='+':
            ac=a+c
        else:
            ac=a-c
        if ac==e:
            answer.append('O')
        else:
            answer.append('X')
    return answer