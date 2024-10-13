def solution(array):
    num = [0] * (max(array)+1)
    for i in array:
        num[i]+=1
    return num.index(max(num)) if num.count(max(num))<2 else -1