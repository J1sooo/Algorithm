def solution(s):
    l1=[]
    answer = 0
    for i in s.split():
        if i=='Z':
            l1.pop()
        else:
            l1.append(int(i))
    return sum(l1)