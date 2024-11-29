def solution(my_string):
    n=''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(map(int,n.split()))