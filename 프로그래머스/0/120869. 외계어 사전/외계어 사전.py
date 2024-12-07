def solution(spell, dic):
    spellSet=set(spell)
    for i in dic:
        if spellSet.issubset(i):
            return 1
    return 2
    