def solution(numbers):
    answer = ''
    s1=''
    eng=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in numbers:
        s1+=i
        if s1 in eng:
            answer+=str(eng.index(s1))
            s1=''
    return int(answer)