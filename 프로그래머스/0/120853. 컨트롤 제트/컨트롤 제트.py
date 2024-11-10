def solution(s):
    l1=[]
    answer = 0
    for i in s.split():
        if i.lstrip('-').isdigit():
            l1.append(int(i))
        elif i=='Z':
            l1.pop()
    return sum(l1)