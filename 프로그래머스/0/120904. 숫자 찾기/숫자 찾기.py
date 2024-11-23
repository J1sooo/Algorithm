def solution(num, k):
    num,k=str(num),str(k)
    return num.index(k)+1 if k in num else -1