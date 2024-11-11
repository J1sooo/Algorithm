def solution(sides):
    sides=sorted(sides)
    a,b,c=sides
    if a+b>c:
        return 1
    else:
        return 2