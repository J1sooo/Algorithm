def solution(dots):
    mx2, my2=max(dots)
    mx1, my1=min(dots)
    return (mx2-mx1)*(my2-my1)