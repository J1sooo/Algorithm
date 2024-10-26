def solution(rsp):
    rspans={'2':'0','0':'5','5':'2'}
    return ''.join(rspans[i] for i in rsp)