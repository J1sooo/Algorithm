def solution(array, n):
    l1=[]
    array.sort()
    for i in array:
        l1.append(abs(i-n))
    
    return array[(l1.index(min(l1)))]