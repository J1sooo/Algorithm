def solution(dots):
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]
    
    if ((y2-y1)/(x2-x1)==(y4-y3)/(x4-x3))or((y3-y1)/(x3-x1)==(y4-y2)/x4-x2)or((y4-y1)/(x4-x1)==(y3-y2)/(x3-x2)):
        return 1
    else:
        return 0
