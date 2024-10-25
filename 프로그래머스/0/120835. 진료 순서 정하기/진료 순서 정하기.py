def solution(emergency):
    l1 = sorted(emergency, reverse=True)
    return [l1.index(i)+1 for i in emergency]