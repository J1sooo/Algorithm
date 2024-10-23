def solution(age):
    answer = ''
    ac = [i for i in range(ord('a'),ord('j')+1)]
    for i in str(age):
        answer+=chr(ac[int(i)])
    return answer