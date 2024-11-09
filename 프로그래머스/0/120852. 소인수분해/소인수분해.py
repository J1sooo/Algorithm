def solution(n):
    answer = []
    so=2
    while n>1:
        if n%so==0:
            answer.append(so)
            while n%so==0:
                n//=so
        so+=1
    return answer